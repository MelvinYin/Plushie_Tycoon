package plushie_tycoon.global;

import plushie_tycoon.global.geGlobal.GEGlobal;

public class GlobalMain {
    public static void main(String[] args) throws Exception {
        int publicPortno = 50002;
        int adminPortno = 50003;
        GEGlobal ge = new GEGlobal(publicPortno, adminPortno);
        ge.runGlobalServer();
        ge.runAdminServer();
    }
}
