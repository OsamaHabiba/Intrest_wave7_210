void ip()
{

     
        auto filename = "impactParameter.csv";
        auto df = ROOT::RDF::MakeCsvDataFrame(filename);

        auto ip = df.Histo1D({"ip","Impact Parameter", 10,0,500},"ip");
        TCanvas *c1 = new TCanvas{};

        ip-> DrawClone();

}

