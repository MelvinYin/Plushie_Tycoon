package plushie_tycoon.serverService.geGlobal;

import plushie_tycoon.serverService.geGlobal.GlobalServerService;

public class GlobalServer {
    public static void main(String[] args) throws Exception {
        int portno = 50001;
        GlobalServerService service = new GlobalServerService(portno);
        service.run();
    }
}
