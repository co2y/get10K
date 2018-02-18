from bs4 import BeautifulSoup
import requests
import re
import random

request_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

search_url = "https://www.last10k.com/Search?q="

symbols = ["PIH", "TURN", "FCCY", "SRCE", "ABIL", "ANCX", "ACNB", "AGFS", "AGFSW", "ABTX", "AMR", "AMRWW", "AMBC", "AMBCW", "ATAX", "AMNB", "ANAT", "AMRB", "ABCB", "AMSF", "ASRV", "ASRVP", "ATLO", "AFSI", "ANCB", "ANDA", "ANDAR", "ANDAU", "ANDAW", "ACGL", "ACGLO", "ACGLP", "AGII", "AGIIL", "AROW", "ASFI", "ATAC", "ATACR", "ATACU", "AAME", "ACBI", "ACFC", "ATLC", "AFH", "AFHBL", "AUBN", "BWINA", "BWINB", "BANF", "BANFP", "BCTF", "BOCH", "BMRC", "BMLP", "BKSC", "BOTJ", "OZRK", "BFIN", "BWFG", "BANR", "DFVL", "DFVS", "DLBL", "DLBS", "DTUL", "DTUS", "DTYL", "DTYS", "FLAT", "STPP", "TAPR", "BHAC", "BHACR", "BHACU", "BHACW", "BYBK", "BCBP", "BSF", "BNCL", "BGCP", "BRPA", "BRPAR", "BRPAU", "BRPAW", "BCAC", "BCACR", "BCACU", "BCACW", "BRAC", "BRACR", "BRACU", "BRACW", "HAWK", "BCOR", "BHBK", "BOFI", "BOFIL", "BOKF", "BOKFL", "BOMN", "BPFH", "BPFHP", "BPFHW", "BDGE", "BHF", "BYFC", "BPY", "BRKL", "BMTC", "BLMT", "CFFI", "CATC", "CAC", "CCBG", "CFFN", "CSTR", "CARO", "CART", "CARV", "CATY", "CATYW", "CBFV", "CBOE", "CBTX", "CSFL", "CFBK", "CVCY", "CNBKA", "CHFN", "CHFC", "CHMG", "CCCR", "JRJC", "HGSH", "CLDC", "CINF", "CZNC", "CZWI", "CZFC", "CIZN", "CHCO", "CIVB", "CIVBP", "CSBK", "CMSS", "CMSSR", "CMSSU", "CMSSW", "CME", "CCNE", "CWAY", "COBZ", "CVLY", "CIGI", "CBAN", "COLB", "CBSH", "CBSHP", "ESXB", "CFBI", "CTBI", "CWBC", "CNFR", "CNOB", "CNAC", "CNACR", "CNACU", "CNACW", "CPSS", "CRVL", "ICBK", "COWN", "COWNZ", "PMTS", "CACC", "DGLD", "DSLV", "GLDI", "SLVO", "TVIX", "TVIZ", "UGLD", "USLV", "USOI", "VIIX", "VIIZ", "XIV", "ZIV", "CRESY", "CVBF", "DHIL", "DCOM", "DNBF", "DGICA", "DGICB", "LYL", "DOTA", "DOTAR", "DOTAU", "DOTAW", "ETFC", "EBMT", "EGBN", "EFBI", "EWBC", "EHTH", "ELEC", "ELECU", "ELECW", "ESBK", "EMCI", "EMCF", "ECPG", "ESGR", "ENFC", "EBTC", "EFSC", "EQFN", "EQBK", "ERIE", "ESQ", "ESSA", "EEFT", "FANH", "FMAO", "FFKT", "FMNB", "FBSS", "FSAC", "FSACU", "FSACW", "FNHC", "FFBW", "FDBC", "LION", "FITB", "FITBI", "FNGN", "FISI", "FNTE", "FNTEU", "FNTEW", "FBNC", "FNLC", "BUSE", "FBIZ", "FCAP", "FCNCA", "FCBC", "FCCO", "FBNK", "FDEF", "FFBC", "FFBCW", "FFIN", "THFF", "FFNW", "FFWM", "FGBI", "FHB", "INBK", "INBKL", "FIBK", "FRME", "FMBH", "FMBI", "FNWB", "FSFG", "FUNC", "FUSB", "FSV", "FFIC", "FNBG", "FRPH", "FSBW", "FSBC", "FULT", "GABC", "GBCI", "GLBZ", "GBLI", "GBLIL", "GBLIZ", "GPAQU", "GSHT", "GSHTU", "GSHTW", "GOV", "GOVNI", "GSBC", "GNBC", "GCBC", "GLRE", "GRIF", "GGAL", "GTYH", "GTYHU", "GTYHW", "GBNK", "GNTY", "GFED", "GWGH", "HALL", "HBK", "HLNE", "HBHC", "HBHCL", "HAFC", "HONE", "HWBK", "HYAC", "HYACU", "HYACW", "HIIQ", "HTLF", "HNNA", "HTBK", "HFWA", "HX", "HMNF", "HBCP", "HOMB", "HFBL", "HMST", "HMTA", "HTBI", "HOPE", "HFBC", "HBNC", "HBMD", "HBAN", "HBANN", "HBANO", "HBANP", "HVBC", "IAM", "IAMXR", "IAMXW", "IBKC", "IBKCO", "IBKCP", "ICCH", "IROQ", "ILG", "INDB", "IBCP", "IBTX", "INDU", "INDUU", "INDUW", "IPCC", "IBKR", "IBOC", "INTL", "ISTR", "ISBC", "ITIC", "JXSB", "JRVR", "JTPY", "KAAC", "KAACU", "KAACW", "KBLM", "KBLMR", "KBLMU", "KBLMW", "KRNY", "KFFB", "KINS", "KNSL", "LSBK", "LBAI", "LKFN", "LCA", "LCAHU", "LCAHW", "LARK", "LCNB", "LTXB", "LACQ", "LACQU", "LACQW", "TREE", "LX", "LOB", "LIVE", "LMFA", "LMFAW", "LPLA", "LBC", "MBTF", "MACQ", "MACQW", "MIII", "MIIIU", "MIIIW", "MCBC", "MFNC", "MGYR", "MHLD", "MSFG", "MLVF", "MKTX", "MRLN", "MPAC", "MPACU", "MPACW", "MBFI", "MBFIO", "MFIN", "MFINL", "MELR", "MBWM", "MBIN", "EBSB", "CASH", "MPB", "MBCN", "MSBI", "MOFG", "MMAC", "MMDM", "MMDMR", "MMDMU", "MMDMW", "MORN", "MSBF", "MTECU", "MUDSU", "MFSF", "MVBF", "NDAQ", "NKSH", "NCOM", "NESR", "NESRW", "NGHC", "NGHCN", "NGHCO", "NGHCP", "NGHCZ", "NHLD", "NHLDW", "NSEC", "NWLI", "JSM", "NAVI", "NBTB", "NEBUU", "UEPS", "NYMTP", "NMRK", "NODK", "NICK", "NCBS", "NMIH", "NBN", "NTRS", "NTRSP", "NFBK", "NRIM", "NWBI", "NWFL", "OVLY", "OCFC", "OFED", "OVBC", "OLBK", "ONB", "OPOF", "OSBC", "OSBCP", "OBAS", "OPHC", "ORIT", "ORRF", "OSPR", "OSPRU", "OSPRW", "OTTW", "OXBR", "OXBRW", "PMBC", "PPBI", "PACW", "PKBK", "PBHC", "PNBK", "PYDS", "PBBI", "PCSB", "PDLB", "PGC", "PWOD", "WRLS", "WRLSR", "WRLSU", "WRLSW", "PEBO", "PEBK", "PFIS", "PBCT", "PBCTP", "PUB", "PICO", "PNFP", "EAGLU", "PLBC", "PBSK", "BPOP", "BPOPM", "BPOPN", "PBIB", "PRAA", "PFBI", "PFG", "PVBC", "PROV", "PBIP", "QCRH", "RNDB", "RBB", "RDFN", "RBNC", "RNST", "RBCAA", "FRBK", "RVSB", "STBA", "SCAC", "SCACU", "SCACW", "SAFT", "SAL", "SASR", "SBFG", "SBFGP", "SBCF", "SNFCA", "SEIC", "SLCT", "SIGI", "STNL", "STNLU", "STNLW", "SFBS", "SVBI", "SHBI", "SIFI", "SIEB", "BSRR", "SBNY", "SBNYW", "SAMG", "SFNC", "SLM", "SLMBP", "SMBK", "SFBC", "SSB", "SFST", "SMBC", "SONA", "SBSI", "SSLJ", "STFC", "STBZ", "STLR", "STLRU", "STLRW", "SBT", "SSFN", "SYBT", "SMMF", "SBBX", "SIVB", "TROW", "AMTD", "TBNK", "TCBI", "TCBIL", "TCBIP", "TCBIW", "TFSL", "TBBK", "CG", "TCGP", "TCFC", "FBMS", "FLIC", "NAVG", "TIL", "TSBK", "TIPT", "TMSR", "TMSRW", "TCBK", "TSC", "TBK", "TRST", "TRMK", "TRCB", "GROW", "UMBF", "UMPQ", "UNAM", "UBSH", "UNB", "UBCP", "UBOH", "UBSI", "UCBA", "UCBI", "UCFC", "UBNK", "UFCS", "UIHC", "UBFO", "UNTY", "UVSP", "VALU", "VEAC", "VEACU", "VEACW", "VBTX", "VCTR", "VBFC", "VIRT", "VRTS", "VRTSP", "WAFD", "WAFDW", "WASH", "WSBF", "WCFB", "WEBK", "WSBC", "WTBA", "WABC", "WNEB", "WLTW", "WINS", "WTFC", "WTFCM", "WTFCW", "WETF", "WMIH", "WRLD", "WSFS", "WVFC", "YIN", "ZAIS", "ZION", "ZIONW", "ZIONZ"]

# random.shuffle(symbols)
# print(symbols)

def run():
    for symbol in symbols[:10]:
        r = requests.get(search_url + symbol, headers = request_headers)
        content = r.text
        soup = BeautifulSoup(content, 'lxml')
        reports = soup.select('#reportLinksList10K')
        download(reports, '2012')

def download(reports, year):
    for report in reports:
        infos = report.find_all('li')
        for info in infos:
            if repr(info.get_text()).find(year) > 0:
                data_cik = info['data-cik']
                data_accessionno = info['data-accessionno'].replace('-', '')
                data_filename = info['data-filename'] + '.doc'
                # https://www.last10k.com/sec-filings/1591890/000138713117001422/pih-10k_123116.htm.doc
                # https://www.last10k.com/sec-filings/1591890/000138713115001018/pih-10k_123114.htm.doc
                download_url = "https://www.last10k.com/sec-filings/" + data_cik + '/' + data_accessionno + '/' + data_filename
                print(download_url)
                d = requests.get(download_url, headers = request_headers)
                with open(data_filename.replace('.htm', ''), "wb") as f:
                    f.write(d.content)

if __name__ == '__main__':
    run()
