from art import Art
from gmsab import save_s3, save_db
import random

if __name__ == '__main__':
    random.seed(None)
    generated = Art(size=2**11)
    print("Making art with the seed %s" % repr(generated.x))
    art_data = generated.redraw()
    print("saved to %s (Size %s)\nSEED: %s" % (art_data['filename'], art_data['size'], repr(art_data['seed'])))

    # save the generated image for the online viewer
    if save_s3(art_data) == 0:
        save_db(art_data)
