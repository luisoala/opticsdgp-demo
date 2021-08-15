import gradio as gr
import numpy as np
from processingpipeline.pipeline import RawProcessingPipeline
from processingpipeline.torch_pipeline import raw2rgb, RawToRGB, ParametrizedProcessing, NNProcessing

#current_dir = "/home/donald/Documents/research/perturbed-minds-project/opticsdgp-demo"

def process(raw_img):
  #raw_dataset = get_dataset('DS') #TODO: input from selection (show an example)
  #raw_img = load_image(path)
  
  #loader = torch.utils.data.DataLoader(raw_dataset, batch_size=1)
  #batch_raw, batch_mask = next(iter(loader))

  # torch proc
  #camera_parameters = raw_dataset.camera_parameters
  #black_level = camera_parameters[0]

  #proc = ParametrizedProcessing(camera_parameters) #TODO: write two other classes and write in 

  #batch_rgb = proc(batch_raw)
  #rgb = batch_rgb[0]
  return raw_img #rgb_img

def sepia(img):
  sepia_filter = np.array([[.393, .769, .189],
                           [.349, .686, .168],
                           [.272, .534, .131]])
  sepia_img = img.dot(sepia_filter.T)
  sepia_img /= sepia_img.max()                          
  return sepia_img


iface = gr.Interface(process, gr.inputs.Image(shape=(256, 256)), "image",examples=[
        ["drone_1.png"]
    ])
iface.launch(share=True)

