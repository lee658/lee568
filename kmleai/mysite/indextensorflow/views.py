from django.http import HttpResponse
from django.shortcuts import render
import tensorflow as tf
import numpy as np

def test(request):
    return render(request, 'indextensorflow/page_error.html')

def index(request):
    #a = run_inference_on_image()
    #return HttpResponse(a)
    return render(request, 'indextensorflow/index.html')

'''
imagePath = '/workspace/kmleai/mysite/media/tensorflow/testImg.jpg'          # 추론을 진행할 이미지 경로
modelFullPath = '/tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = '/tmp/output_labels.txt'                                   # 읽어들일 labels 파일 경로

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
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        result = [human_string, score]
        return result
'''