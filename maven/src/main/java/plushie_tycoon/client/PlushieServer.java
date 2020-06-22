package plushie_tycoon.client;

import plushie_tycoon.client.clientEngine.ClientEngine;

public class PlushieServer {
    public static void main(String[] args) throws Exception {
        int webPagePortno = 50001;
        int serverPortno = 50002;
        ClientEngine ge = new ClientEngine(webPagePortno, serverPortno);
        ge.initFromGlobalServer();
        ge.runServices();
    }
}
