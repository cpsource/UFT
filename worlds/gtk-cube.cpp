#include <gtk/gtk.h>
#include <cairo.h>

// Draw callback for drawing the cube
gboolean on_draw_event(GtkWidget *widget, cairo_t *cr, gpointer user_data) {
    // Define cube vertices in 2D space for an isometric projection
    double vertices[8][2] = {
        {100, 100},  // 0: Top front left
        {200, 100},  // 1: Top front right
        {200, 200},  // 2: Bottom front right
        {100, 200},  // 3: Bottom front left
        {150, 150},  // 4: Top back left
        {250, 150},  // 5: Top back right
        {250, 250},  // 6: Bottom back right
        {150, 250}   // 7: Bottom back left
    };

    // Set line width for better visibility
    cairo_set_line_width(cr, 2.0);

    // Draw the front face in blue
    cairo_set_source_rgb(cr, 0.0, 0.0, 1.0);  // Blue color
    cairo_move_to(cr, vertices[0][0], vertices[0][1]);
    cairo_line_to(cr, vertices[1][0], vertices[1][1]);
    cairo_line_to(cr, vertices[2][0], vertices[2][1]);
    cairo_line_to(cr, vertices[3][0], vertices[3][1]);
    cairo_close_path(cr);
    cairo_stroke(cr);

    // Draw the back face in green
    cairo_set_source_rgb(cr, 0.0, 0.5, 0.0);  // Green color
    cairo_move_to(cr, vertices[4][0], vertices[4][1]);
    cairo_line_to(cr, vertices[5][0], vertices[5][1]);
    cairo_line_to(cr, vertices[6][0], vertices[6][1]);
    cairo_line_to(cr, vertices[7][0], vertices[7][1]);
    cairo_close_path(cr);
    cairo_stroke(cr);

    // Draw the connecting lines in black
    cairo_set_source_rgb(cr, 0.0, 0.0, 0.0);  // Black color
    cairo_move_to(cr, vertices[0][0], vertices[0][1]);
    cairo_line_to(cr, vertices[4][0], vertices[4][1]);
    cairo_move_to(cr, vertices[1][0], vertices[1][1]);
    cairo_line_to(cr, vertices[5][0], vertices[5][1]);
    cairo_move_to(cr, vertices[2][0], vertices[2][1]);
    cairo_line_to(cr, vertices[6][0], vertices[6][1]);
    cairo_move_to(cr, vertices[3][0], vertices[3][1]);
    cairo_line_to(cr, vertices[7][0], vertices[7][1]);
    cairo_stroke(cr);

    return FALSE;
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *drawing_area;

    gtk_init(&argc, &argv);

    // Create main window
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "2D Cube Drawing with GTK");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 400);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Create drawing area widget
    drawing_area = gtk_drawing_area_new();
    gtk_container_add(GTK_CONTAINER(window), drawing_area);

    // Connect draw signal to the drawing callback
    g_signal_connect(G_OBJECT(drawing_area), "draw", G_CALLBACK(on_draw_event), NULL);

    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}

