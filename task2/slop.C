void slop()
{


        auto filename = "slops.csv";
        auto df = ROOT::RDF::MakeCsvDataFrame(filename);

        auto ip = df.Histo2D({"slp","slopes",20,-0.5,0.5, 20,-0.5,0.5},"XZ","YZ");
        TCanvas *c1 = new TCanvas{};

        ip-> DrawClone("lego2");

}

