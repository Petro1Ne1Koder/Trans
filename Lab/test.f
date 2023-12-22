program myprogram {
    int a;
    int b;
    int c;
    float x;
    int i;
    bool y;

    a = 2;
    b = 5;
    input(a);
    input(b);
    a = a + 3;
    b = b * 2;
    output(a, b);
    a = a -2;
    b = b / 3;
    x = a ^ b;
    i = 0;
    if (x >= 2) {
          output(x);
    }
    while (i <= 5) {
        if (x >= 2) {
            output(x);
            }
        i = i + 1;
    }
    y = true;
}