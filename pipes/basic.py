import torch
from diffusers import StableDiffusionPipeline

GUIDANCE_SCALE_VALUES = [.2, .35, .5, .65, .8]
NUM_INFERENCE_STEPS_VALUES = [2, 4, 8, 16, 32]

def basicPipe():
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)
    pipe.to("cuda")
    pipe.safety_checker = lambda images, **kwargs: (images, False)
    return pipe

def usePipe(pipe, prompt, guidance_scale, num_inference_steps, manual_seed=None):
    if manual_seed is not None:
        generator = torch.Generator("cuda").manual_seed(manual_seed)
    else:
        generator = torch.Generator("cuda")
    return pipe(prompt, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps, generator=generator).images[0]



