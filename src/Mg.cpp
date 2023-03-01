#include "TMultiGraph.h"
#include "TLegend.h"
#include "TGraph.h"
#include "TH1F.h"

#include "iostream"

using namespace std;

class mymg
{
    private :
        TMultiGraph *mg1 = new TMultiGraph();
        TLegend *l1 = new TLegend();
        bool isLegend = true;
    
    public:
        
        // TLegend *l1 = new TLegend(.2,.2,.6,.4);

        mymg()
        {
            mg1 = new TMultiGraph();
            l1 = new TLegend(.6,.7,.85,.85);
            // l1 = new TLegend(.2,.2,.6,.4);
            // l1 = new TLegend();
            // SetMG();
        }
        
        void Add(TGraph *g1, string mytext = "") 
        {
            mg1->Add(g1);
            // TLegend *l1 = new TLegend(.2,.2,.6,.4);
            if(mytext != "")
            {
                l1->AddEntry(g1,mytext.c_str());
                l1->SetBorderSize(0);
                // l1->SetTextSize(0.03);
            }
        }
        void SetMG(char* xtitle, char* ytitle, float xmin, float xmax, float ymin, float ymax)
        {
            mg1->GetHistogram()->SetXTitle(xtitle);
            mg1->GetHistogram()->SetYTitle(ytitle);   
            mg1->GetXaxis()->SetLimits(xmin,xmax);
            mg1->SetMinimum(ymin);
            mg1->SetMaximum(ymax);
            mg1->GetXaxis()->SetLabelSize(0.045);
            mg1->GetYaxis()->SetLabelSize(0.045);
            mg1->GetXaxis()->SetTitleSize(0.04);
            mg1->GetYaxis()->SetTitleSize(0.04);
            mg1->GetXaxis()->SetTitleOffset(1.2);
            mg1->GetYaxis()->SetTitleOffset(1.2);
        }
        void SetTitle(char* mytitle)
        {
            // mg1->SetTitle(mytitle);
            mg1->GetHistogram()->SetTitle(mytitle);
        }
        void Draw()
        {
            // TCanvas *c1 = new TCanvas();

            mg1->Draw("apl");
            // mg1->Draw("ap");
            if(isLegend)
            {
                l1->SetBorderSize(1);
                // l1->SetTextSize(1.);
                l1->SetTextSizePixels(20);
                l1->Draw();
            } 
        }

        void offLegend(){ isLegend = false; }
};