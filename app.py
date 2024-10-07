import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

# Load the pre-trained Stable Diffusion model from Hugging Face
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

# Check if a GPU is available and move the model to the GPU for faster inference
if torch.cuda.is_available():
    pipe = pipe.to("cuda")
else:
    print("CUDA is not available, using CPU. Image generation might be slower.")

# Define a function that will generate the image based on the prompt
def generate_image(prompt):
    # Generate an image using the pipeline with the user prompt
    image = pipe(prompt).images[0]
    return image

# Create a Gradio interface
interface = gr.Interface(
    fn=generate_image,  # The function that generates the image
    inputs="text",      # Input type (text prompt from user)
    outputs="image",    # Output type (generated image)
    title="DreamWeaver",
    description="Enter a text prompt to generate an image with Stable Diffusion",
)

# Launch the app
interface.launch()   