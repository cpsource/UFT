#include <QApplication>
#include <QWidget>
#include <QPainter>

class CubeWidget : public QWidget {
public:
    CubeWidget(QWidget *parent = nullptr) : QWidget(parent) {
        setWindowTitle("2D Cube Drawing with Qt");
        resize(400, 400);
    }

protected:
    void paintEvent(QPaintEvent *event) override {
        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);

        // Define the 3D cube vertices in 2D space
        QPointF vertices[8] = {
            QPointF(100, 100),  // 0: Top front left
            QPointF(200, 100),  // 1: Top front right
            QPointF(200, 200),  // 2: Bottom front right
            QPointF(100, 200),  // 3: Bottom front left
            QPointF(150, 150),  // 4: Top back left
            QPointF(250, 150),  // 5: Top back right
            QPointF(250, 250),  // 6: Bottom back right
            QPointF(150, 250)   // 7: Bottom back left
        };

        // Draw the front face
        painter.setPen(Qt::blue);
        painter.drawLine(vertices[0], vertices[1]);
        painter.drawLine(vertices[1], vertices[2]);
        painter.drawLine(vertices[2], vertices[3]);
        painter.drawLine(vertices[3], vertices[0]);

        // Draw the back face
        painter.setPen(Qt::darkGreen);
        painter.drawLine(vertices[4], vertices[5]);
        painter.drawLine(vertices[5], vertices[6]);
        painter.drawLine(vertices[6], vertices[7]);
        painter.drawLine(vertices[7], vertices[4]);

        // Draw the connecting lines
        painter.setPen(Qt::black);
        painter.drawLine(vertices[0], vertices[4]);
        painter.drawLine(vertices[1], vertices[5]);
        painter.drawLine(vertices[2], vertices[6]);
        painter.drawLine(vertices[3], vertices[7]);
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    CubeWidget cubeWidget;
    cubeWidget.show();

    return app.exec();
}

