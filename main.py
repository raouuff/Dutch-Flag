import tkinter as tk
import random
def DUTCH_FLAG(balls):
    low = 0
    high = len(balls) - 1
    mid = 0
    while mid <= high:
            ################# animation code######################################
            color_canvas.delete("all")
            # Draw labels for indices below each cell
            draw_indices(len(balls))
            # Draw labels for lo, mid, and hi values
            draw_values(low, mid, high)
            # Draw pointers
            draw_low_high_pointers("lo", low)
            draw_mid_pointer("mid", mid)
            draw_low_high_pointers("hi", high)
            # After 5000 milliseconds, call move_ballsow to update the ballsow position
            color_canvas.after(5000, move_ballsow)
            ################# animation code######################################
            #################algorthim logic###################################### 
            swap_message = ""
            # If the element is 'R'
            if balls[mid] == 'R':
            ################# animation code######################################
                draw_colors_with_oval(balls, color_canvas)
                color_canvas.update()
                if balls[mid] != balls[low]:
                    draw_swap_message(color_canvas, balls[mid], mid, balls[low], low)
            ################# animation code######################################
                balls[low], balls[mid] = balls[mid], balls[low]
                low += 1
                mid +=  1
            # If the element is 'W'
            elif balls[mid] == 'W':
            ################# animation code######################################
                draw_colors_with_oval(balls, color_canvas)
                color_canvas.update()
            ################# animation code######################################
                mid+=  1
            # If the element is 'B'
            else:
            ################# animation code######################################
                draw_colors_with_oval(balls, color_canvas)
                color_canvas.update()
                # Swap and draw the swap message
                if balls[mid] != balls[high]:
                    draw_swap_message(color_canvas, balls[mid], mid, balls[high], high)
            ################# animation code######################################
                balls[mid], balls[high] = balls[high], balls[mid]
                high -=  1
            #################algorthim logic###################################### 
            # Draw the colors
            draw_colors_with_oval(balls, color_canvas)
            color_canvas.update()
            # After 5000 milliseconds, call perform_sort again
            color_canvas.after(5000)
    if mid==high or mid>high:draw_sort_completed_message(color_canvas)


def draw_sort_completed_message(canvas):
    x = 350
    y = 300
    canvas.create_text(x, y, text="Sorting is completed", font=('Helvetica', 14), tags='sort_completed_message')
def draw_swap_message(canvas, value1, index1, value2, index2):
    message = f"Swapping {value1} at index {index1} with {value2} at index {index2}"
    x = 350
    y = 250
    canvas.create_text(x, y, text=message, font=('Helvetica', 12), tags='swap_message')
def draw_low_high_pointers(name, position):
        x = 100+position * 50 + 25
        y1 = 170
        y2 = 185
        color_canvas.create_line(x, y1, x, y2, width=2, tags=name)
        color_canvas.create_text(x, y2 + 5, text=name, font=('Helvetica', 8), tags=name)
def draw_mid_pointer(name, position):
        x = 100+position * 50 + 25
        y1 = 70
        y2 = 90
        color_canvas.create_line(x, y1, x, y2 + 20, width=2, tags=name)
        color_canvas.create_text(x, y1 - 5, text=name, font=('Helvetica', 8), tags=name)
def draw_indices(size):
        for i in range(size):
            color_canvas.create_text(100+i * 50 + 25, 160, text=str(i), font=('Helvetica', 8))
def draw_values(lo_val, mid_val, hi_val):
        color_canvas.create_text(200, 50, text=f'lo: {lo_val}', font=('Helvetica', 15), tags='lo')
        color_canvas.create_text(300, 50, text=f'mid: {mid_val}', font=('Helvetica', 15), tags='mid')
        color_canvas.create_text(400, 50, text=f'hi: {hi_val}', font=('Helvetica', 15), tags='hi')
def move_ballsow():
        color_canvas.delete("ballsow")
def draw_colors_with_oval(colors, canvas):
    color_mapping = {'R': 'red', 'W': 'white', 'B': 'blue'}

    element_width = 50
    element_height = 50
    start_x = 100
    start_y = 100
    for i in range(len(colors)):
        color = colors[i]

        x = start_x+i * element_width 
        y =start_y

        # Draw the box
        canvas.create_rectangle(x, y, x + element_width, y + element_height, fill='white', outline='black')

        # Draw the oval inside the box
        oval_radius = 20
        oval_center_x = (x + x + element_width) / 2
        oval_center_y = (y + y + element_height) / 2
        canvas.create_oval(
            oval_center_x - oval_radius, oval_center_y - oval_radius,
            oval_center_x + oval_radius, oval_center_y + oval_radius,
            fill=color_mapping[color], outline='black'
        )
def enter():
    size = int(entry.get())
    global balls
    # Ensure that the ballsay contains all three colors
    while True:
        balls = random.choices(['R', 'W', 'B'], k=size)
        if set(balls) == {'R', 'W', 'B'}:
            draw_colors_with_oval(balls,color_canvas)
            break
def start():
        DUTCH_FLAG(balls)
# Example usage:
root = tk.Tk()
root.geometry("700x500")
root.title("Dutch Flag Problem Visualization")
# Create a canvas
# Place the canvas at the center of the screen
# Entry for ballsay size
entry_label = tk.Label(root, text="Enter ballsay Size:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()
# Enter button
enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()
# Start button
start_button = tk.Button(root, text="Start", command=start)
start_button.pack()
color_canvas = tk.Canvas(root, width=700, height=400, bg='#ffA')
color_canvas.pack()
root.mainloop()
