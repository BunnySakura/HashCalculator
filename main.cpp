#include <iostream>
#include <fstream>

#include "hash_algorithms.h"

#include "wx/wx.h"
#include "show_my_frame.h"

class MyApp : public wxApp {

public:
    MyApp() {}
    virtual ~MyApp() {}
    virtual bool OnInit();
    virtual int OnExit() { return 0; }

};

IMPLEMENT_APP(MyApp);

inline bool MyApp::OnInit() {
    //Init main Frame
    wxFrame* mainFrame = new ShowMyFrame(NULL);
    mainFrame->Show(true);
    SetTopWindow(mainFrame);

    return true;
}

