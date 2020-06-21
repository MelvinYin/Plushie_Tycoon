package plushie_tycoon.global;

import plushie_tycoon.global.globalEngine.GlobalEngine;

public class GlobalMain {
    public static void main(String[] args) throws Exception {
        int portno = 50002;
        GlobalEngine ge = new GlobalEngine(portno);
        ge.runServices();
    }
}
