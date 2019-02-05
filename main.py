from art import Art
import random

if __name__ == '__main__':
    random.seed(None)
    generated = Art(size=2**8)
    print("Making art with the seed %s" % repr(generated.x))
    artData = generated.redraw()
    print("saved to %s (Size %s)\nSEED: %s" % (artData['filename'], artData['size'], repr(artData['seed'])))
