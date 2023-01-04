#include "TGraph.h"
#include "TGraphErrors.h"
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

const float constmarkersize = .8;
const float constlinewidth = 1;

TGraph* onegraph_1(string fileYname, string fileXname);
TGraphErrors* onegraph_1_1(string fileYname, string fileXname);
TGraph* onegraph_2(string fileYname, string fileXname);
TGraph* onegraph_3(string fileYname);
void LoadGraph();

void eachresult(string fileYname, string fileXname, char* output);
void Plots_Only_Revision(mymg *mine);
void Plots_originNrevision(mymg *mine);
void Plots_Jul_time(mymg *mine);
void Plots_flux_order(mymg *mige);
void Plots_Prague(mymg *mine);
void Plots_pragueNrevision(mymg *mg1, mymg *mg2);
void Plots_TR23(mymg *mine);
void Plots_comp3(mymg *mg1, mymg *mg2, mymg *mg3);

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

TGraph  *gApr_origin_dose_thrs,
        *gApr_revision_dose_thrs, 
        *gJun_origin_dose_thrs, 
        *gJun_revision_dose_thrs, 
        *gJul_RPI_origin_dose_thrs, 
        *gJul_RPI_revision_dose_thrs, 
        *gJul_RAS_origin_dose_thrs, 
        *gJul_RAS_revision_dose_thrs, 
        *gSep_origin_dose_thrs, 
        *gSep_revision_dose_thrs,
        *gNov_revision_dose_thrs; 

TGraph  *gRPI_dose_time, *gRAS_dose_time;

TGraph  *gApr_flux_order, 
        *gJun_flux_order, 
        *gJul_flux_order, 
        *gSep_flux_order;

TGraph  *gprague_1,     //5
        *gprague_2,     //16
        *gprague_3,     //17
        *gprague_4,     //19
        *gprague_5,     //38
        *gprague_6,     //41
        *gprague_7;     //42
        
TGraph  *gTR23;

void dose_thrs()
{
    TCanvas *c1= new TCanvas();    
    mymg *mg = new mymg();
    mymg *mg2 = new mymg();
    LoadGraph();

    // Plots_Only_Revision(mg);
    // Plots_originNrevision(mg);
    Plots_Jul_time(mg);
    // Plots_flux_order(mg);
    // Plots_Prague(mg);
    // Plots_pragueNrevision
    // Plots_TR23(mg);
    // Plots_comp3(mg,mg,mg);

    // mg->offLegend();
    // mg->SetMG("Dose(krad)","Mean Threshold",0,100,0,200);
    mg->SetMG("Time(min)","Mean Threshold",0,600,0,200);
    mg->Draw();
    
    c1->SetGrid();
    // c1->SetLogy();
}



void LoadGraph()
{
    string mypath = "/home/suchoi/KOMAC/analysis/processed/";
    string mypath2 = "/home/suchoi/KOMAC/analysis/prague/";
    string mypath3 = "/home/suchoi/KOMAC/analysis/TR23/tr23.txt";

    gApr_origin_dose_thrs         = onegraph_1(mypath + "datainfo/mean_Apr_origin.txt"      ,mypath + "dose/Apr_dose.txt");
    gJun_origin_dose_thrs         = onegraph_1(mypath + "datainfo/mean_Jun_origin.txt"      ,mypath + "dose/Jun_dose.txt");
    gJul_RPI_origin_dose_thrs     = onegraph_1(mypath + "datainfo/mean_Jul_RPI_origin.txt"  ,mypath + "dose/Jul_RPI_dose.txt");
    gJul_RAS_origin_dose_thrs     = onegraph_1(mypath + "datainfo/mean_Jul_RAS_origin.txt"  ,mypath + "dose/Jul_RAS_dose.txt");
    gSep_origin_dose_thrs         = onegraph_1(mypath + "datainfo/mean_Sep_origin.txt"      ,mypath + "dose/Sep_dose.txt");
    
    gApr_revision_dose_thrs       = onegraph_1(mypath + "datainfo/mean_Apr_revision.txt"    ,mypath + "dose/Apr_dose.txt");
    gJun_revision_dose_thrs       = onegraph_1(mypath + "datainfo/mean_Jun_revision.txt"    ,mypath + "dose/Jun_dose.txt");
    gJul_RPI_revision_dose_thrs   = onegraph_1(mypath + "datainfo/mean_Jul_RPI_revision.txt",mypath + "dose/Jul_RPI_dose.txt");
    gJul_RAS_revision_dose_thrs   = onegraph_1(mypath + "datainfo/mean_Jul_RAS_revision.txt",mypath + "dose/Jul_RAS_dose.txt");
    gSep_revision_dose_thrs       = onegraph_1(mypath + "datainfo/mean_Sep_revision.txt"    ,mypath + "dose/Sep_dose.txt");
    gNov_revision_dose_thrs       = onegraph_1(mypath + "datainfo/mean_Nov_revision.txt"    ,mypath + "dose/Nov_dose.txt");


    // gApr_revision_dose_thrs       = onegraph_1_1(mypath + "datainfo/mean_Apr_revision.txt"    ,mypath + "dose/Apr_dose.txt");
    // gJun_revision_dose_thrs       = onegraph_1_1(mypath + "datainfo/mean_Jun_revision.txt"    ,mypath + "dose/Jun_dose.txt");
    // gJul_RPI_revision_dose_thrs   = onegraph_1_1(mypath + "datainfo/mean_Jul_RPI_revision.txt",mypath + "dose/Jul_RPI_dose.txt");
    // gJul_RAS_revision_dose_thrs   = onegraph_1_1(mypath + "datainfo/mean_Jul_RAS_revision.txt",mypath + "dose/Jul_RAS_dose.txt");
    // gSep_revision_dose_thrs       = onegraph_1_1(mypath + "datainfo/mean_Sep_revision.txt"    ,mypath + "dose/Sep_dose.txt");

    gRPI_dose_time       = onegraph_2(mypath + "datainfo/mean_Jul_RPI_revision.txt", mypath + "scantime/Jul_RPI_time.txt");
    gRAS_dose_time       = onegraph_2(mypath + "datainfo/mean_Jul_RAS_revision.txt", mypath + "scantime/Jul_RAS_time.txt");

    // gApr_flux_order      = onegraph(mypath + "flux/Apr_flux.txt");
    // gJun_flux_order      = onegraph(mypath + "flux/Jun_flux.txt");
    // gJul_flux_order      = onegraph(mypath + "flux/Jul_flux.txt");
    // gSep_flux_order      = onegraph(mypath + "flux/Sep_flux.txt");
    
    gprague_1           = onegraph_3(mypath2+"r5.txt");
    gprague_2           = onegraph_3(mypath2+"r16.txt");
    gprague_3           = onegraph_3(mypath2+"r17.txt");
    gprague_4           = onegraph_3(mypath2+"r19.txt");
    gprague_5           = onegraph_3(mypath2+"r38.txt");
    gprague_6           = onegraph_3(mypath2+"r41.txt");
    gprague_7           = onegraph_3(mypath2+"r42.txt");

    gTR23 = onegraph_3(mypath3);
}

void eachresult(string fileYname, string fileXname, char* output)
{
    TCanvas *c1 = new TCanvas();
    TGraph *g1 = onegraph_1(fileYname,fileXname);

    
    SetGraph(g1,1);
    
    g1->Draw();
    c1->SaveAs(output);
}

//For revision and original thrs
TGraph* onegraph_1(string fileYname, string fileXname)
{
    TGraph *g1 = new TGraph();

    ifstream fileY;
        ifstream fileX;
        fileY.open(fileYname);
        fileX.open(fileXname);

        if(!fileY) cout << "there is no file : " << fileYname << endl;
        if(!fileX) cout << "there is no file : " << fileXname << endl;

        string line1, line2;
        float accumX = 0;
        fileX >> line1;     // for column titl1
        fileY >> line2;     // for column title
        while(1)
        {
            double_t valY, valX, x, y;

            fileY >> line1;
            fileX >> line2;
            if(fileY.eof()) break;

            valX = stof(line2);
            valY = stof(line1.substr(0,line1.find(',')));
            
        
            accumX += valX;
            x = accumX;
            y = valY * 10;
                
            g1->SetPoint(g1->GetN(),x,y);    
        }

        fileY.close();
        fileX.close();

    return g1;
}

TGraphErrors* onegraph_1_1(string fileYname, string fileXname)
{
    TGraphErrors *g1 = new TGraphErrors();

    ifstream fileY;
        ifstream fileX;
        fileY.open(fileYname);
        fileX.open(fileXname);

        if(!fileY) cout << "there is no file : " << fileYname << endl;
        if(!fileX) cout << "there is no file : " << fileXname << endl;

        string line1, line2;
        float accumX = 0;
        fileX >> line1;     // for column titl1
        fileY >> line2;     // for column title
        while(1)
        {
            double_t valY, valX,valE, x, y, error;
            // string valE;

            fileY >> line1;
            fileX >> line2;
            if(fileY.eof()) break;

            valX = stof(line2);
            valY = stof(line1.substr(0,line1.find(',')));
            valE = stof(line1.substr(line1.find(',')+1,line1.length()-line1.find(',')));
            

            accumX += valX;
            x = accumX;
            y = valY * 10;
            error = valE * 10;
                
            int graphorder = g1->GetN();
            g1->SetPoint(graphorder,x,y);
            g1->SetPointError(graphorder,0,error);
        }

        fileY.close();
        fileX.close();

    return g1;
}

//For Dose time
TGraph* onegraph_2(string fileYname, string fileXname)
{
    TGraph *g1 = new TGraph();

    ifstream fileY;
    ifstream fileX;
    fileY.open(fileYname);
    fileX.open(fileXname);

    if(!fileY) cout << "there is no file : " << fileYname << endl;
    if(!fileX) cout << "there is no file : " << fileXname << endl;

    string line1, line2;
    float accumX = 0;
    fileX >> line1;     // for column titl1
    fileY >> line2;     // for column title
    while(1)
    {
        double_t valY, valX, x, y;
        fileY >> line1;
        fileX >> line2;
        if(fileY.eof()) break;

        valX = stof(line2);
        valY = stof(line1.substr(0,line1.find(',')));
        
        x = valX;
        y = valY * 10;
            
        g1->SetPoint(g1->GetN(),x,y);    
    }

        fileY.close();
        fileX.close();

    return g1;
}

// For Prague
TGraph* onegraph_3(string fileYname)
{
    TGraph *g1 = new TGraph();
    
    ifstream fileY;
    fileY.open(fileYname);
    
    if(!fileY) cout << "there is no file : " << fileYname << endl;
    
    string line1, line2;
    int order=1;
    fileY >> line1;  // for column title
        
    // cout << line << endl;
    while(1)
    {
        double_t valX,valY, x,y;

        fileY >> line1;
        // cout << "line : " << line1 << endl;
        if(fileY.eof()) break;
        
        // if(line.find(',') != string::npos)  // if it has ','
        // {
        //     valY = line.substr(0,line.find(','));
        //     valX = line.substr(0,line.find(','));
        //     double_t x,y;
        //     // cout << "there is comma" << endl;
        //     y = stof(valY);
        //     x = stof(valX);
        //     g1->SetPoint(g1->GetN(),x,y);    
        
        // }
        // else
        
        fileY >> line2;
        valX = stof(line1);
        valY = stof(line2);

        y = valY;
        x = valX;
        // cout << x << "," << y << endl;
        // x = order;
        g1->SetPoint(g1->GetN(),x,y);    
        // order++;
        
        
    }
    fileY.close();
    return g1;
}

    // if(fileXname == "default")
    // {
    //     ifstream fileY;
    //     fileY.open(fileYname);
    
    //     if(!fileY) cout << "there is no file : " << fileYname << endl;
        
    //     string valX,valY, line;
    //     int order=1;
    //     fileY >> line;  // for column title
        
    //     // cout << line << endl;
    //     while(1)
    //     {
    //         fileY >> line;
    //         cout << line << endl;
    //         if(fileY.eof()) break;
            
    //         if(line.find(',') != string::npos)  // if it has ','
    //         {
    //             valY = line.substr(0,line.find(','));
    //             valX = line.substr(0,line.find(','));
    //             double_t x,y;
    //             // cout << "there is comma" << endl;
    //             y = stof(valY);
    //             x = stof(valX);
    //             g1->SetPoint(g1->GetN(),x,y);    
            
    //         }
    //         else
    //             valY = line;
    //             double_t x,y;
    //             // cout << "there is not comma" << endl;
    //             // cout << valX << "," << valY << endl;
    //             y = stof(valY);
    //             x = order;
    //             g1->SetPoint(g1->GetN(),x,y);    

    //             order++;
            
            
    //     }

    //     fileY.close();
    // }

    // else
    // {
    //     ifstream fileY;
    //     ifstream fileX;
    //     fileY.open(fileYname);
    //     fileX.open(fileXname);

    //     if(!fileY) cout << "there is no file : " << fileYname << endl;
    //     if(!fileX) cout << "there is no file : " << fileXname << endl;

    //     string valY, valX, line1, line2;
    //     float accumX = 0;
    //     fileX >> line1;     // for column title
    //     fileY >> line2;     // for column title
    //     while(1)
    //     {
    //         fileY >> line1;
    //         fileX >> line2;
    //         if(fileY.eof()) break;

    //         if(line1.find(',') != string::npos)  // if it has ','
    //         {
    //             valY = line1.substr(0,line1.find(','));
    //             cout << "there is comma" << endl;
    //         }
    //         else    
    //             valY = line1;
    //         if(line2.find(',') != string::npos)  // if it has ','
    //         {
    //             valX = line1.substr(0,line2.find(','));
    //         }
    //         else    
    //             valX = line2;

    //         double_t x,y;
    //         if(isaccum)
    //         {
    //             accumX += stof(valX);
    //             x = accumX;
    //             y = stof(valY) * 10;
    //         }
    //         else
    //         {
    //             x = stof(valX);
    //             y = stof(valY) * 10;
    //         }        

    //         g1->SetPoint(g1->GetN(),x,y);    
    //     }

    //     fileY.close();
    //     fileX.close();
    // }


void Plots_Only_Revision(mymg *mine) // **** Only Revision ****
{
    SetGraph(gApr_revision_dose_thrs,kRed);
    SetGraph(gJun_revision_dose_thrs,kOrange);
    SetGraph(gJul_RPI_revision_dose_thrs,kGreen);
    SetGraph(gJul_RAS_revision_dose_thrs,kBlue);
    SetGraph(gSep_revision_dose_thrs,kBlue+2);
    SetGraph(gNov_revision_dose_thrs,kViolet);
    
    mine->Add(gApr_revision_dose_thrs,"2022-04");
    mine->Add(gJun_revision_dose_thrs,"2022-06");
    mine->Add(gJul_RPI_revision_dose_thrs,"2022-07(separated)");
    mine->Add(gJul_RAS_revision_dose_thrs,"2022-07");
    mine->Add(gSep_revision_dose_thrs,"2022-09");
    mine->Add(gNov_revision_dose_thrs,"2022-11");
}

void Plots_originNrevision(mymg *mine)
{
    //-------------------------------------------------------------------------
    // **** Origin vs Revision ****
    //-------------------------------------------------------------------------
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

    mine->Add(gApr_origin_dose_thrs,"2022-04, origin");
    mine->Add(gApr_revision_dose_thrs,"2022-04, revision");
    mine->Add(gJun_origin_dose_thrs,"2022-06, origin");
    mine->Add(gJun_revision_dose_thrs,"2022-06, revision");
    mine->Add(gJul_RPI_origin_dose_thrs,"2022-07(separated), origin");
    mine->Add(gJul_RPI_revision_dose_thrs,"2022-07(separated), revision");
    mine->Add(gJul_RAS_origin_dose_thrs,"2022-07, origin");
    mine->Add(gJul_RAS_revision_dose_thrs,"2022-07, revision");
    mine->Add(gSep_origin_dose_thrs,"2022-09, origin");
    mine->Add(gSep_revision_dose_thrs,"2022-09, revision");
}

void Plots_Jul_time(mymg *mine)
{
    //-------------------------------------------------------------------------
    // **** RPI RAS Time grapg ****
    //-------------------------------------------------------------------------
    SetGraph(gRAS_dose_time,kBlue);
    SetGraph(gRPI_dose_time,kGreen);

    mine->Add(gRAS_dose_time,"Continuous Irradiated");
    mine->Add(gRPI_dose_time,"Separated after a few irradiations");
}

void Plots_flux_order(mymg *mine)
{
    //-------------------------------------------------------------------------
    // **** Flux order ****
    //-------------------------------------------------------------------------
    SetGraph(gApr_flux_order,kRed);
    SetGraph(gJun_flux_order,kOrange);
    SetGraph(gJul_flux_order,kBlue);
    SetGraph(gSep_flux_order,kViolet);

    mine->Add(gApr_flux_order,"2022-04");
    mine->Add(gJun_flux_order,"2022-06");
    mine->Add(gJul_flux_order,"2022-07");
    mine->Add(gSep_flux_order,"2022-09");
}

void Plots_Prague(mymg *mine)
{
    //-------------------------------------------------------------------------
    // **** Prague Plot ****
    //-------------------------------------------------------------------------
    SetGraph(gprague_1,kGreen);
    SetGraph(gprague_2,kBlue);
    SetGraph(gprague_3,kRed);
    SetGraph(gprague_4,kCyan);
    SetGraph(gprague_5,kBlack);
    SetGraph(gprague_6,kYellow-6);
    SetGraph(gprague_7,kViolet);

    mine->Add(gprague_1);
    mine->Add(gprague_2);
    mine->Add(gprague_3);
    mine->Add(gprague_4);
    mine->Add(gprague_5);
    mine->Add(gprague_6);
    mine->Add(gprague_7);
}

void Plots_TR23(mymg *mine)
{
    SetGraph(gTR23,kBlack);

    mine->Add(gTR23);
}

void Plots_pragueNrevision(mymg *mg1, mymg *mg2)
{
    Plots_Prague(mg1);
    Plots_Only_Revision(mg2);

    TPad *p1 = new TPad("p1","p1",0, .5, 1., 1.);
    TPad *p2 = new TPad("p2","p2",0,  0, 1., .5);
    p1->Draw();
    p2->Draw();
    p1->cd();

    
    mg1->SetMG("Dose(krad)","Mean Threshold",0,350,0,200);
    mg1->Draw();

    p2->cd();
    mg2->SetMG("Dose(krad)","Mean Threshold",0,350,0,200);
    mg2->Draw();
    p1->SetGrid();
    p2->SetGrid();

}

void Plots_comp3(mymg *mg1, mymg *mg2, mymg *mg3)
{
    int color_prague    = kBlack;
    int color_TR23      = kGray;
    
    mg2 = mg1;
    mg3 = mg1;

    SetGraph(gprague_1,color_prague);
    SetGraph(gprague_2,color_prague);
    SetGraph(gprague_3,color_prague);
    SetGraph(gprague_4,color_prague);
    SetGraph(gprague_5,color_prague);
    SetGraph(gprague_6,color_prague);
    SetGraph(gprague_7,color_prague);

    mg1->Add(gprague_1,"Prague");
    mg1->Add(gprague_2);
    mg1->Add(gprague_3);
    mg1->Add(gprague_4);
    mg1->Add(gprague_5);
    mg1->Add(gprague_6);
    mg1->Add(gprague_7);

    SetGraph(gTR23,color_TR23);

    mg2->Add(gTR23,"TR23");

    SetGraph(gApr_revision_dose_thrs,       kRed);
    SetGraph(gJun_revision_dose_thrs,       kOrange);
    SetGraph(gJul_RPI_revision_dose_thrs,   kGreen);
    SetGraph(gJul_RAS_revision_dose_thrs,   kBlue);
    SetGraph(gSep_revision_dose_thrs,       kViolet);

    // SetGraph(gApr_revision_dose_thrs,       color_tr102);
    // SetGraph(gJun_revision_dose_thrs,       color_tr102);
    // SetGraph(gJul_RPI_revision_dose_thrs,   color_tr102);
    // SetGraph(gJul_RAS_revision_dose_thrs,   color_tr102);
    // SetGraph(gSep_revision_dose_thrs,       color_tr102);
    
    mg3->Add(gApr_revision_dose_thrs,"2022-04");
    mg3->Add(gJun_revision_dose_thrs,"2022-06");
    mg3->Add(gJul_RPI_revision_dose_thrs,"2022-07(seperated)");
    mg3->Add(gJul_RAS_revision_dose_thrs,"2022-07");
    mg3->Add(gSep_revision_dose_thrs,"2022-09");

}


