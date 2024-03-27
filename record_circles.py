import matplotlib.pyplot as plt

def draw_circles(diameters_cm, output_file_name):
    fig, ax = plt.subplots(figsize=(11.7, 16.5))  # A3 paper size in inches

    # Draw each circle
    for diameter in diameters_cm:
        circle_radius_mm = (diameter / 2) * 10  # Convert radius from cm to mm
        circle = plt.Circle((0, 0), circle_radius_mm, fill=False, edgecolor='blue', linewidth=1.5)
        ax.add_artist(circle)

    # Set plot limits to avoid clipping, adjusted based on the largest circle
    largest_radius_mm = max(diameters_cm) * 10 / 2
    ax.set_xlim(-largest_radius_mm * 1.1, largest_radius_mm * 1.1)
    ax.set_ylim(-largest_radius_mm * 1.1, largest_radius_mm * 1.1)
    ax.set_aspect('equal', 'box')  # Ensure circles are perfectly circular
    plt.axis('off')  # Remove axes for clarity

    # Save the figure as a PDF file
    plt.savefig(output_file_name, dpi=300, format='pdf', bbox_inches='tight')
    plt.close(fig)  # Close the figure to free up memory

# Updated diameters in cm for each record size
diameters_12_inch = [12*2.54, 11.5*2.54, ((4+(3/4))*2.54), ((4+(5/32))*2.54), ((3+(3/4))*2.54), 0.73]
diameters_10_inch = [10*2.54, 9.5*2.54, ((4+(3/4))*2.54), ((4+(5/32))*2.54), ((3+(3/4))*2.54), 0.73]
diameters_7_inch = [7*2.54, (6+(5/8))*2.54, ((4+(1/4))*2.54), ((3+(51/64))*2.54), ((3+(15/32))*2.54), 0.73]

# Generate the PDFs
draw_circles(diameters_12_inch, 'record_12".pdf')
draw_circles(diameters_10_inch, 'record_10".pdf')
draw_circles(diameters_7_inch, 'record_7".pdf')
