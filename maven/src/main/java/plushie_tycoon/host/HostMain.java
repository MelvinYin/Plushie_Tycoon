package plushie_tycoon.host;

import plushie_tycoon.host.hostEngine.HostEngine;

public class HostMain {
    public static void main(String[] args) throws Exception {
        int portno = 50002;
        HostEngine ge = new HostEngine(portno);
        ge.runServices();
    }
}
