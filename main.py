#!/usr/bin/evn python

from engine import RenderEngine
from scene_loader import load_scene
from multiprocessing import cpu_count
import time

def main():

    process_count = cpu_count()
    print(f"Process count{process_count}")

    tic = time.perf_counter()
    scene = load_scene('./scenes/2balls.json')
    engine = RenderEngine()

    with open("2balls.ppm", "w") as img_file:
        engine.render_multiprocess(scene, process_count, img_file)

    toc = time.perf_counter()
    print(f"Rendering completed in {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()