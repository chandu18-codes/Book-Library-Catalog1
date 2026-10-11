class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }
    void erase() {
        System.out.println("Erasing a shape");
    }

    class Circle extends Shape {
        void draw() {
            System.out.println("Drawing a circle");
        }
        void erase() {
            System.out.println("Erasing a circle");
        }

    class Triangle extends Shape {
        void draw() {
            System.out.println("Drawing a triangle");
        }
        void erase() {
            System.out.println("Erasing a triangle");
        }

    class Square extends Shape {
        void draw() {
            System.out.println("Drawing a square");
        }
        void erase() {
            System.out.println("Erasing a square");
        }
    }
    }
    }
    public static void main(String[] args) {
        Shape shape = new Shape();
        Circle shape1 = new Circle();
        Triangle shape2 = new Triangle();
        Square shape3 = new Square();
        shape.draw();
        shape.erase();
        shape1.draw();
        shape1.erase();
        shape2.draw();
        shape2.erase();
        shape3.draw();
        shape3.erase();
    }
    
}
