#include "TGraph.h"
#include "TCanvas.h"
#include "TString.h"
#include "TH1F.h"
#include "TColor.h"
#include "TPad.h"
#include "TPaveLabel.h"

#include "iostream"
#include "fstream"
#include "string"

#include "src/Mg.cpp"

using namespace std;


const int xmax = 70;
const int xmin = 0;
const int ymax = 150;
const int ymin = 0;

const float constmarkersize = 1.;
const float constlinewidth = 1;

void SetGraph(TGraph *mygraph,int mycolor,int mymarkerstyle = 20,float mymarkersize = constmarkersize, float mylinewidth = constlinewidth);
TGraph* onegraph(string fileYname, string fileXname = "default", bool isaccum=false);
void LoadGraph();
void eachresult(string fileYname, string fileXname, char* output);

TGraph  *gApr_origin_dose_thrs,
        *gApr_revision_dose_thrs, 
        *gJun_origin_dose_thrs, 
        *gJun_revision_dose_thrs, 
        *gJul_RPI_origin_dose_thrs, 
        *gJul_RPI_revision_dose_thrs, 
        *gJul_RAS_origin_dose_thrs, 
        *gJul_RAS_revision_dose_thrs, 
        *gSep_origin_dose_thrs, 
        *gSep_revision_dose_thrs; 

TGraph  *gRPI_dose_time, *gRAS_dose_time;

TGraph  *gApr_flux_order, 
        *gJun_flux_order, 
        *gJul_flux_order, 
        *gSep_flux_order;
        

void dose_thrs()
{
    TCanvas *c1= new TCanvas();
    
    mymg *mg = new mymg();
    LoadGraph();
    SetGraph(gApr_origin_dose_thrs,kBlack);
    SetGraph(gApr_revision_dose_thrs,kRed);
    SetGraph(gJun_origin_dose_thrs,kBlack);
    SetGraph(gJun_revision_dose_thrs,kOrange);
    SetGraph(gJul_RPI_origin_dose_thrs,kBlack);
    SetGraph(gJul_RPI_revision_dose_thrs,kGreen);
    SetGraph(gJul_RAS_origin_dose_thrs,kBlack);
    SetGraph(gJul_RAS_revision_dose_thrs,kBlue);
    SetGraph(gSep_origin_dose_thrs,kBlack);
    SetGraph(gSep_revision_dose_thrs,kViolet);

    SetGraph(gRAS_dose_time,kRed);
    SetGraph(gRPI_dose_time,kBlueYellow);

    SetGraph(gApr_flux_order,kRed);
    SetGraph(gJun_flux_order,kOrange);
    SetGraph(gJul_flux_order,kBlue);
    SetGraph(gSep_flux_order,kViolet);

    // mg->Add(gApr_origin_dose_thrs,"2022-04, origin");
    // mg->Add(gApr_revision_dose_thrs,"2022-04, revision");
    // mg->Add(gJun_origin_dose_thrs,"2022-06, origin");
    // mg->Add(gJun_revision_dose_thrs,"2022-06, revision");
    // mg->Add(gJul_RPI_origin_dose_thrs,"2022-07(seperated), origin");
    // mg->Add(gJul_RPI_revision_dose_thrs,"2022-07(seperated), revision");
    // mg->Add(gJul_RAS_origin_dose_thrs,"2022-07, origin");
    // mg->Add(gJul_RAS_revision_dose_thrs,"2022-07, revision");
    // mg->Add(gSep_origin_dose_thrs,"2022-09, origin");
    // mg->Add(gSep_revision_dose_thrs,"2022-09, revision");
    
    // mg->Add(gApr_revision_dose_thrs,"2022-04");
    // mg->Add(gJun_revision_dose_thrs,"2022-06");
    // mg->Add(gJul_RPI_revision_dose_thrs,"2022-07(seperated)");
    // mg->Add(gJul_RAS_revision_dose_thrs,"2022-07");
    // mg->Add(gSep_revision_dose_thrs,"2022-09");

    mg->Add(gRAS_dose_time,"RAS");
    mg->Add(gRPI_dose_time,"RPI");

    // mg->Add(gApr_flux_order,"2022-04");
    // mg->Add(gJun_flux_order,"2022-06");
    // mg->Add(gJul_flux_order,"2022-07");
    // mg->Add(gSep_flux_order,"2022-09");
    


    // mg->offLegend();
    mg->SetMG("time(min)","mean threshold",0,500,1,200);
    
    mg->Draw();
    
    // c1->SetLogy();
}



void LoadGraph()
{
    string mypath = "/home/suchoi/KOMAC/analysis/processed/";

    gApr_origin_dose_thrs         = onegraph(mypath + "datainfo/mean_Apr_origin.txt"      ,mypath + "dose/Apr_dose.txt",                0);
    gApr_revision_dose_thrs       = onegraph(mypath + "datainfo/mean_Apr_revision.txt"    ,mypath + "dose/Apr_dose.txt",                0);
    gJun_origin_dose_thrs         = onegraph(mypath + "datainfo/mean_Jun_origin.txt"      ,mypath + "dose/Jun_dose.txt",                0);
    gJun_revision_dose_thrs       = onegraph(mypath + "datainfo/mean_Jun_revision.txt"    ,mypath + "dose/Jun_dose.txt",                0);
    gJul_RPI_origin_dose_thrs     = onegraph(mypath + "datainfo/mean_Jul_RPI_origin.txt"  ,mypath + "dose/Jul_RPI_dose.txt",   0);
    gJul_RPI_revision_dose_thrs   = onegraph(mypath + "datainfo/mean_Jul_RPI_revision.txt",mypath + "dose/Jul_RPI_dose.txt",   0);
    gJul_RAS_origin_dose_thrs     = onegraph(mypath + "datainfo/mean_Jul_RAS_origin.txt"  ,mypath + "dose/Jul_RAS_dose.txt",   0);
    gJul_RAS_revision_dose_thrs   = onegraph(mypath + "datainfo/mean_Jul_RAS_revision.txt",mypath + "dose/Jul_RAS_dose.txt",   0);
    gSep_origin_dose_thrs         = onegraph(mypath + "datainfo/mean_Sep_origin.txt"      ,mypath + "dose/Sep_dose.txt",                0);
    gSep_revision_dose_thrs       = onegraph(mypath + "datainfo/mean_Sep_revision.txt"    ,mypath + "dose/Sep_dose.txt",                0);

    gRPI_dose_time       = onegraph(mypath + "datainfo/mean_Jul_RPI_revision.txt", mypath + "scantime/Jul_RPI_time.txt");
    gRAS_dose_time       = onegraph(mypath + "datainfo/mean_Jul_RAS_revision.txt", mypath + "scantime/Jul_RAS_time.txt");

    gApr_flux_order      = onegraph(mypath + "flux/Apr_flux.txt");
    gJun_flux_order      = onegraph(mypath + "flux/Jun_flux.txt");
    gJul_flux_order      = onegraph(mypath + "flux/Jul_flux.txt");
    gSep_flux_order      = onegraph(mypath + "flux/Sep_flux.txt");
}



void eachresult(string fileYname, string fileXname, char* output)
{
    TCanvas *c1 = new TCanvas();
    TGraph *g1 = onegraph(fileYname,fileXname,0);

    
    SetGraph(g1,1);
    
    g1->Draw();
    c1->SaveAs(output);
}

TGraph* onegraph(string fileYname, string fileXname = "default", bool isaccum=false)
{
    TGraph *g1 = new TGraph();
    
    if(fileXname == "default")
    {
        ifstream fileY;
        fileY.open(fileYname);
    
        if(!fileY) cout << "there is no file : " << fileYname << endl;
        
        string valY, line;
        int order=1;
        fileY >> line;  // for column title
        // cout << line << endl;
        while(1)
        {
            fileY >> line;
            if(fileY.eof()) break;
            
            if(line.find(',') != string::npos)  // if it has ','
            {
                valY = line.substr(0,line.find(','));
            }
            else
                valY = line;
            
            double_t x,y;
            y = stof(valY);
            x = order;
            g1->SetPoint(g1->GetN(),x,y);    
            
            order++;
        }

        fileY.close();
    }

    else
    {
        ifstream fileY;
        ifstream fileX;
        fileY.open(fileYname);
        fileX.open(fileXname);

        if(!fileY) cout << "there is no file : " << fileYname << endl;
        if(!fileX) cout << "there is no file : " << fileXname << endl;

        string valY, valX, line1, line2;
        float accumX = 0;
        fileX >> line1;     // for column title
        fileY >> line2;     // for column title
        while(1)
        {
            fileY >> line1;
            fileX >> line2;
            if(fileY.eof()) break;

            if(line1.find(',') != string::npos)  // if it has ','
            {
                valY = line1.substr(0,line1.find(','));
            }
            else    
                valY = line1;
            if(line2.find(',') != string::npos)  // if it has ','
            {
                valX = line1.substr(0,line2.find(','));
            }
            else    
                valX = line2;

            double_t x,y;
            if(isaccum)
            {
                accumX += stof(valX);
                x = accumX;
                y = stof(valY) * 10;
            }
            else
            {
                x = stof(valX);
                y = stof(valY) * 10;
            }        

            g1->SetPoint(g1->GetN(),x,y);    
        }

        fileY.close();
        fileX.close();
    }
    

    return g1;
}

void SetGraph(TGraph *mygraph,int mycolor,int mymarkerstyle = 20,float mymarkersize = constmarkersize, float mylinewidth = constlinewidth)
{
    mygraph->SetMarkerStyle(20);
    mygraph->SetMarkerSize(mymarkersize);
    mygraph->SetLineWidth(mylinewidth);
    mygraph->SetMarkerColor(mycolor);
    mygraph->SetLineColor(mycolor);
    mygraph->GetXaxis()->SetLimits(xmin,xmax);
    mygraph->SetMinimum(ymin);
    mygraph->SetMaximum(ymax);
}
