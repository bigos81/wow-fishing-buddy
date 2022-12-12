from pyautogui import *
from imagesearch import *
import time
from msvcrt import getch


#mardraxux / bonefish
buff = 'buff-maldrax.png'
bobber = 'bobber.png'

#anderwwald / Iridescent Amberjack
#buff = 'buff-ander.png'
#bobber = 'bober-ander.png'

#wampirki / Spinefin Piranha
#buff = 'buff-vamp.png'
#bobber = 'bobber-vamp.png'

#bastion
#buff = 'buff-vamp.png'
#bbobber = 'bober-bastion.png'


def main():
    start_t = time.time()
    all_casts = 0
    caugth = 0
    print('any key to start...')
    getch()
    start = time.time() - 50000
    fails = 0
    while 1:
        all_casts = all_casts + 1
        if time.time() - start > 29 * 60:
            if not have_buff():
                use_bite_from_bags()
                start = time.time()
        if not catch():
            fails = fails + 1
        else:
            caugth = caugth + 1
            fails = 0
        elapsed = time.time() - start_t
        print('Casts {0}, Success {1}, Percentage {2}, Elapsed {3:.2f} [m], Fish per min {4:.2f}'.format(all_casts, caugth, int(caugth*100/all_casts), elapsed/60, caugth*60/elapsed), end='\r')
        if fails > 10:
            exit(5)
        time.sleep(2 + random.random())


def catch():

    fishing_skill_coords = imagesearch('fishing-skill-icon.png', 0.8)
    if fishing_skill_coords[0] == -1:
        print("can't find the fishing skill icon to  click")
        exit(1)
    moveTo(fishing_skill_coords[0] + 10, fishing_skill_coords[1] + 10)
    long_click_here()
    moveTo(fishing_skill_coords[0] - 30, fishing_skill_coords[1] + 10)

    time.sleep(3)

    orig_bobber_coords = imagesearch(bobber, 0.6)
    if orig_bobber_coords[0] == -1:
        return False

    now = time.time()

    while 1:
        bobber_coorrds = imagesearch(bobber, 0.6)
        if time.time() - now > 19:
            break
        dx = abs(orig_bobber_coords[0] - bobber_coorrds[0])
        dy = abs(orig_bobber_coords[1] - bobber_coorrds[1])
        if dx > 100 or dy > 100:
            moveTo(orig_bobber_coords[0] + 25, orig_bobber_coords[1] + 25)
            long_click_here()
            time.sleep(0.1)
            if imagesearch('nofish.png')[0] == -1:
                return True
            return False
    moveTo(fishing_skill_coords[0] - 30, fishing_skill_coords[1] + 10)
    return False


def use_bite_from_bags():
    bait_coords = imagesearch('use-bait.png', 0.8)
    if bait_coords[0] == -1:
        print("can't find bait macro")
        exit(2)
    mouseDown(x=bait_coords[0] + 5, y=bait_coords[1] + 5, button=PRIMARY, duration=0.5)
    mouseUp(button=PRIMARY)


def have_buff():
    return True
    buff_coords = imagesearch(buff, 0.8)
    return buff_coords[0] != -1


def long_click_here():
    mouseDown()
    time.sleep(0.25)
    mouseUp()


if __name__ == "__main__":
    main()
