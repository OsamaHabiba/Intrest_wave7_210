void mult()
{


        auto filename = "mult.csv";
        auto df = ROOT::RDF::MakeCsvDataFrame(filename);

        auto ip = df.Histo1D({"mult","Multiplicity", 10,0,20},"mult");
        TCanvas *c1 = new TCanvas{};

        ip-> DrawClone();

}


