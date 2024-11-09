#include <gtk/gtk.h>
#include <cairo.h>
#include <math.h>

// Define constants for the cube size and rotation speed
#define CUBE_SIZE 50
#define ROTATION_SPEED 0.05

// Rotation angle
static double rotation_angle = 0;

// Function to rotate a point in 3D and project onto 2D
void rotate_and_project(double x, double y, double z, double *out_x, double *out_y) {
    // Rotation around Y-axis
    double rotated_x = x * cos(rotation_angle) - z * sin(rotation_angle);
    double rotated_z = x * sin(rotation_angle) + z * cos(rotation_angle);

    // Projecting 3D coordinates to 2D (simple orthographic projection)
    *out_x = rotated_x;
    *out_y = y;
}

// Drawing callback function
gboolean on_draw_event(GtkWidget *widget, cairo_t *cr, gpointer user_data) {
    // Define the original 3D vertices of the cube
    double vertices[8][3] = {
        {-CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE},  // 0: Top front left
        { CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE},  // 1: Top front right
        { CUBE_SIZE,  CUBE_SIZE, -CUBE_SIZE},  // 2: Bottom front right
        {-CUBE_SIZE,  CUBE_SIZE, -CUBE_SIZE},  // 3: Bottom front left
        {-CUBE_SIZE, -CUBE_SIZE,  CUBE_SIZE},  // 4: Top back left
        { CUBE_SIZE, -CUBE_SIZE,  CUBE_SIZE},  // 5: Top back right
        { CUBE_SIZE,  CUBE_SIZE,  CUBE_SIZE},  // 6: Bottom back right
        {-CUBE_SIZE,  CUBE_SIZE,  CUBE_SIZE}   // 7: Bottom back left
    };

    // Array to hold the 2D projected vertices
    double projected[8][2];

    // Project each vertex to 2D after rotating
    for (int i = 0; i < 8; i++) {
        rotate_and_project(vertices[i][0], vertices[i][1], vertices[i][2], &projected[i][0], &projected[i][1]);
    }

    // Center the cube on the canvas
    cairo_translate(cr, 200, 200);

    // Set line width for visibility
    cairo_set_line_width(cr, 2.0);

    // Draw front face in blue
    cairo_set_source_rgb(cr, 0.0, 0.0, 1.0);  // Blue
    cairo_move_to(cr, projected[0][0], projected[0][1]);
    cairo_line_to(cr, projected[1][0], projected[1][1]);
    cairo_line_to(cr, projected[2][0], projected[2][1]);
    cairo_line_to(cr, projected[3][0], projected[3][1]);
    cairo_close_path(cr);
    cairo_stroke(cr);

    // Draw back face in green
    cairo_set_source_rgb(cr, 0.0, 0.5, 0.0);  // Green
    cairo_move_to(cr, projected[4][0], projected[4][1]);
    cairo_line_to(cr, projected[5][0], projected[5][1]);
    cairo_line_to(cr, projected[6][0], projected[6][1]);
    cairo_line_to(cr, projected[7][0], projected[7][1]);
    cairo_close_path(cr);
    cairo_stroke(cr);

    // Draw connecting lines in black
    cairo_set_source_rgb(cr, 0.0, 0.0, 0.0);  // Black
    for (int i = 0; i < 4; i++) {
        cairo_move_to(cr, projected[i][0], projected[i][1]);
        cairo_line_to(cr, projected[i + 4][0], projected[i + 4][1]);
    }
    cairo_stroke(cr);

    return FALSE;
}

// Timer callback function to update the rotation and trigger redraw
gboolean update_rotation(gpointer user_data) {
    GtkWidget *widget = GTK_WIDGET(user_data);

    // Increment the rotation angle
    rotation_angle += ROTATION_SPEED;

    // Redraw the widget
    gtk_widget_queue_draw(widget);

    return TRUE;  // Continue calling the timer
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *drawing_area;

    gtk_init(&argc, &argv);

    // Create main window
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Rotating 2D Cube with GTK");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 400);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Create drawing area widget
    drawing_area = gtk_drawing_area_new();
    gtk_container_add(GTK_CONTAINER(window), drawing_area);

    // Connect draw signal to the drawing callback
    g_signal_connect(G_OBJECT(drawing_area), "draw", G_CALLBACK(on_draw_event), NULL);

    // Start the timer to update rotation every 30 ms (for smooth animation)
    g_timeout_add(30, update_rotation, drawing_area);

    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}

