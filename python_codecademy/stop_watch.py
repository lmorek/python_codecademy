
# template for "Stopwatch: The Game"

# define global variables
import simplegui

interval = 100
count = 0
success_stops = 0
all_stops = 0
result = 0
stop = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t//600
    B = (t//100)% 6
    C = (t//10) % 10
    D = t % 10
    string = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return string


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop
    stop = False
    timer.start()

def stop():
    global success_stops, all_stops, count, result, stop
    if stop == False:

        if (count % 10) == 0 and (count !=0):
            success_stops =+1
            all_stops +=1
        elif (count !=0):
            all_stops +=1
        result = str(success_stops) + "/" + str(all_stops)
    stop == True
    timer.stop()
    #return result


def reset():
    global count, result, success_stops, all_stops
    result =0
    count = 0
    success_stops = 0
    all_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    #print count


# define draw handler
def draw(canvas):
    text=format(count)
    canvas.draw_text( text,[125, 125], 25, "Red")
    canvas.draw_text( str(result),[20, 20], 25, "Red")

# create frame
frame = simplegui.create_frame("Stopwatch game", 250, 250)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 75)
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", reset, 75)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()

# Please remember to review the grading rubric
 