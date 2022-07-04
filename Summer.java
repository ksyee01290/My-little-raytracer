import java.util.ArrayList;
import java.io.*;

public class Summer {
    public static void main(String[] args) throws IOException {
        double width = 300;
        double ratio = 16.0 / 9.0;
        double height = (width / ratio);

        String as = "/Users/jeong-geun-won/Desktop/raytracer/test.ppm";
        BufferedWriter bw = new BufferedWriter(new FileWriter(as));

        ppm_header header = new ppm_header();
        present output = new present();

        ArrayList<Integer> sw = output.present(width, ratio);

        try {
            String a = header.ppm_Header(width, height);
            bw.write(a);
            System.out.println(a);
        } catch (Exception e) {
            e.getStackTrace();
        }
        for (int i = 0; i < sw.size(); i++) {
            if (i % 3 == 0) {
                bw.write("\n");
            }
            bw.write(sw.get(i) + " ");
        }
        bw.close();
    }
}

class ppm_header {
    public String ppm_Header(double width, double height) {
        String a = new String("P3\n" + width + " " + height + "\n255");
        return a;
    }
}

class present {
    public ArrayList<Integer> present(double width, double ratio) {
        double height = (width / ratio);
        ArrayList<Integer> out = new ArrayList<>();

        for (int i = 0; i < width * height; i++) {
            out.add(255);
            out.add(123);
            out.add(203);
        }

        return out;
    }
}
