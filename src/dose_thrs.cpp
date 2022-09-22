#include "TGraph.h"
#include "TCanvas.h"
#include "TString.h"
#include "TH1F.h"
#include "TMultiGraph.h"
#include "TLegend.h"
#include "TColor.h"
#include "TPad.h"
#include "TPaveLabel.h"

#include "iostream"
#include "fstream"
#include "string"

using namespace std;


const int xmax = 60;
const int xmin = -5;
const int ymax = 150;
const int ymin = 0;

const float mymarkersize = .8;
const float mylinewidth = 1;


void dose_thrs(string dosetxt, string thrstxt)
{
    ifstream dosefile;
    dosefile.open(dosetxt);

    while(1)
    {
        string temp;
        dosefile >> temp;
        

        if(dosefile.eof()) break;

        double_t x = stof(temp);

        cout << x << endl;
    }


    // TGraph *g1 = new TGraph();

    // string filedir="/Users/hipex/KOMAC/2022-09/RPI/2022-09/";
    // string filename="thrs_dose.txt";
    
    // ifstream thrs_file;
    // thrs_file.open(filedir+filename);

    // if(thrs_file.fail())
    // cout << "there is no thrs_file" << endl;
    // char dose[30];
    // char thrs[30];
    // int mycolors[7] = {kRed,kOrange,kGreen,kBlue,kCyan,kViolet,kMagenta};
    // int i=0;

    // while(1)
    // {
    //     thrs_file >> dose;
    //     thrs_file >> thrs;

    //     if(thrs_file.eof()) break;

    //     double_t x = stof(dose);
    //     double_t y = stof(thrs);

    //     if(y >= 0) g1->SetPoint(g1->GetN(),x,y);
    // }
    // thrs_file.close();

    // g1->SetMarkerStyle(8);
    // g1->SetMarkerSize(mymarkersize);
    // g1->SetLineWidth(mylinewidth);
    // g1->SetMarkerColor(kBlack);
    // g1->SetLineColor(kBlack);

    // g1->Draw();

}
