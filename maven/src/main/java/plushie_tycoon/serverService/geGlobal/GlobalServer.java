package plushie_tycoon.serverService.geGlobal;

import plushie_tycoon.serverService.ServerService;

public class GlobalServer {
    public static void main(String[] args) throws Exception {
        int portno = 50001;
        ServerService service = new ServerService(portno);
        service.run();
    }
}
