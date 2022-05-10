from deepface import DeepFace


    # """
    # This function applies real time face recognition and facial attribute analysis
    # Parameters:
    #     db_path (string): facial database path. You should store some .jpg files in this folder.
    #     model_name (string): VGG-Face, Facenet, OpenFace, DeepFace, DeepID, Dlib or Ensemble
    #     detector_backend (string): opencv, ssd, mtcnn, dlib, retinaface
    #     distance_metric (string): cosine, euclidean, euclidean_l2
    #     enable_facial_analysis (boolean): Set this to False to just run face recognition
    #     source: Set this to 0 for access web cam. Otherwise, pass exact video path.
    #     time_threshold (int): how many second analyzed image will be displayed
    #     frame_threshold (int): how many frames required to focus on face

    # """

  #model_name = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
  #distance_metric = ["cosine", "euclidean", "euclidean_l2"]    

def facnetmode(source,db_path):



    distance_metric = 'euclidean_l2'
    
    #E:\JOB_WORK\scifffers\deepface-master\kabali.mp4
    #E:\JOB_WORK\scifffers\deepface-master\kabali.mp4
    
    enable_face_analysis=False 
    #outputpath=r"E:\JOB_WORK\scifffers\deepface-master\Output_path\opnewgovinda.avi"
    model_name="Facenet"
    detector_backend='opencv'

    DeepFace.stream(model_name=model_name,db_path =db_path,enable_face_analysis = enable_face_analysis,source=source,distance_metric=distance_metric,detector_backend=detector_backend)

source=0
db_path=r"D:\Deepface\deepface-master\database\Actor"
facnetmode(source,db_path)