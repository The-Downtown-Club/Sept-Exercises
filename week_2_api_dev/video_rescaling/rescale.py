import logging
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import os
import ffmpeg
import enlighten


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('enlighten')

BITRATES = {
    360: Bitrate(280 * 1024, 128 * 1024),
    480: Bitrate(432 * 1024, 192 * 1024),
    576: Bitrate(490 * 1024, 192 * 1024),
    720: Bitrate(1320 * 1024, 320 * 1024),
    1080: Bitrate(2048 * 1024, 320 * 1024),
}
RESOLUTIONS = list(BITRATES)

def generate_thumbnail(dirname):
    input_filename = f"{dirname}/original.mp4"
    output_filename = f"{dirname}/thumbnail.jpg"
    if os.path.exists(output_filename):
        LOGGER.debug("Already exists " + output_filename)
    else:
        (
            ffmpeg
            .input(input_filename, ss=0.1)
            .filter('scale', 720, -1)
            .output(output_filename, vframes=1)
            .run()
        )

def get_resolution(input_filename):
    probe = ffmpeg.probe(input_filename)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    return width, height

def get_transformed_resolution(width, height, resolution):
    get_even = lambda x: x + (x%2)
    if width >= height:
        width = (width * resolution) // height
        height = resolution
    else:
        height = (height * resolution) // width
        width = resolution
    return get_even(width), get_even(height)


def get_representations(input_filename, resolutions):
    representations = []
    width, height = get_resolution(input_filename)
    for resolution in resolutions:
        new_width, new_height = get_transformed_resolution(width, height, resolution)
        representations.append(
            Representation(Size(new_width, new_height), BITRATES.get(resolution))
        )
    return representations


def convert_to_m3u8(dirname, resolutions):
    input_filename = f"{dirname}/original.mp4"
    output_filename = f"{dirname}/adaptive.m3u8"
    if os.path.exists(output_filename):
        LOGGER.debug("Already exists " + output_filename)
    else:
        video = ffmpeg_streaming.input(input_filename)
        hls = video.hls(Formats.h264(), hls_list_size=0, hls_time=3, hls_init_time=1)
        representations = get_representations(input_filename, resolutions)
        hls.representations(*representations)
        hls.fragmented_mp4()
        hls.output(output_filename)
        LOGGER.debug(f"Completed {output_filename}")


def main():
    files =  os.listdir('output')
    pbar = enlighten.Counter(total=len(files), desc="Files processed", unit='ticks')
    for dirname in files:
        dirname = f"output/{dirname}"
        if not os.path.exists(f"{dirname}/original.mp4"):
            LOGGER.debug(f"Nothing to process, Skipped {dirname}")
        else:
            generate_thumbnail(dirname)
            convert_to_m3u8(dirname, RESOLUTIONS)
        pbar.update()

if __name__ == '__main__':
    main()