from django.shortcuts import redirect, render
from .models import Examination
from .forms import PostModelForm
from .diag import diagnosis
import os
import tensorflow as tf
import numpy as np

imagePath = '/workspace/kmleai/mysite/media/tensorflow/testImg.jpg'          # 추론을 진행할 이미지 경로
modelFullPath = '/tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = '/tmp/output_labels.txt'
existfile = os.path.isfile('/workspace/kmleai/mysite/media/tensorflow/testImg.jpg')

def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
        

def run_inference_on_image():
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        result = []
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))
            if (human_string == "b'lobar pneumonia\\n'"):
                result.append(['DATA Set 안에 있는 lobar pneumonia의 유사도는 {}입니다.'.format(score*100)])
            if (human_string == "b'broncho pneumonia\\n'"):
                result.append(['DATA Set 안에 있는 broncho pneumonia의 유사도는 {}입니다.'.format(score*100)])
        answer = labels[top_k[0]]
        return result

def examination_form(request):
    print(request)
    
    if os.path.isfile('/workspace/kmleai/mysite/media/tensorflow/testImg.jpg'):
        os.remove('/workspace/kmleai/mysite/media/tensorflow/testImg.jpg')
        form = PostModelForm()
    else:
        if request.method == 'POST':
            print("POST format")
            if request.FILES:
                print("File format")
                form = PostModelForm(request.POST, request.FILES)
                if form.is_valid():
                    tensorflow = form.save()
                    return redirect(tensorflow)
            else:
                print("Non-POST format", request.POST)
                postdata = request.POST
                diagresult = diagnosis(postdata)
                return render(request, 'examination/examination_form.html', {'diagresult':diagresult,})
                
        else:
            form = PostModelForm()
    return render(request, 'examination/examination_form.html', {
        'form': form,
    })

def examination_detail(request, pk):
    examination = Examination.objects.get(pk=pk)
    a = run_inference_on_image()
    return render(request, 'examination/examination_detail.html', {'a':a,}, {
        'examination': examination,
    })


'''
def examination_form(request):
    print(request)
    
    if os.path.isfile('/workspace/kmleai/mysite/media/tensorflow/testImg.jpg'):
        os.remove('/workspace/kmleai/mysite/media/tensorflow/testImg.jpg')
        form = PostModelForm()
    else:
        if request.method == 'POST':
            print("POST format")
            if request.FILES:
                print("File format")
                form = PostModelForm(request.POST, request.FILES)
                if form.is_valid():
                    tensorflow = form.save()
                    return redirect(tensorflow)
            else:
                print("Non-POST format", request.GET)
                # print(request.content_params)
                print(request.POST['count'])
                data = {}
                for i in range(int(request.POST['count'])):
                    tmp = chr(97+i)
                    data[tmp] = request.POST[tmp]
                return render(request, 'examination/examination_form.html', {
                    'data': data
                })
'''
