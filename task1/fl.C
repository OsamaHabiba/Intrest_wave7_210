void fl()
{

        TH1F *flightlength = new TH1F{"fl", "Flight Length", 10, 0, 5000};

	auto filename = "flightlength.csv";
	auto df = ROOT::RDF::MakeCsvDataFrame(filename);
	
	auto fl = df.Histo1D({"fl","Flight Length", 10,0,5000},"length");
        TCanvas *c1 = new TCanvas{};

        fl-> DrawClone();

}

