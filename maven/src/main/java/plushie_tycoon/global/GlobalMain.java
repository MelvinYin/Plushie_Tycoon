package plushie_tycoon.global;

import plushie_tycoon.global.geGlobal.GEGlobal;

public class GlobalMain {
    public static void main(String[] args) throws Exception {
        int portno = 50002;
        GEGlobal ge = new GEGlobal(portno);
        ge.runServices();
    }
}
