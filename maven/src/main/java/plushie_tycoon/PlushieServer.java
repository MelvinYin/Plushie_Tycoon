package plushie_tycoon;

import plushie_tycoon.local.localEngine.LocalEngine;

public class PlushieServer {
    public static void main(String[] args) throws Exception {
        int webPagePortno = 50001;
        int serverPortno = 50002;
        LocalEngine ge = new LocalEngine(webPagePortno, serverPortno);
        ge.initFromGlobalServer();
        ge.runServices();
    }
}
