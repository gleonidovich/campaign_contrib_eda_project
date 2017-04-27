import pandas as pd

cand_party_dict = { "P00003392":"DEMOCRATIC",
                    "P20002671":"LIBERTARIAN",
                    "P20002721":"REPUBLICAN",
                    "P20003281":"REPUBLICAN",
                    "P20003984":"GREEN",
                    "P40003576":"REPUBLICAN",
                    "P60003670":"REPUBLICAN",
                    "P60005915":"REPUBLICAN",
                    "P60006046":"REPUBLICAN",
                    "P60006111":"REPUBLICAN",
                    "P60006723":"REPUBLICAN",
                    "P60007168":"DEMOCRATIC",
                    "P60007242":"REPUBLICAN",
                    "P60007572":"REPUBLICAN",
                    "P60007671":"DEMOCRATIC",
                    "P60007697":"REPUBLICAN",
                    "P60008059":"REPUBLICAN",
                    "P60008398":"REPUBLICAN",
                    "P60008521":"REPUBLICAN",
                    "P60008885":"INDEPENDENT",
                    "P60009685":"DEMOCRATIC",
                    "P60022654":"INDEPENDENT",
                    "P80001571":"REPUBLICAN",
                    "P80003379":"REPUBLICAN",
                    "P80003478":"REPUBLICAN" }

cmte_nm_dict = {"C00458844":"MARCO RUBIO FOR PRESIDENT",
                "C00500587":"PERRY FOR PRESIDENT INC",
                "C00573519":"CARSON AMERICA",
                "C00574624":"CRUZ FOR PRESIDENT",
                "C00575449":"RAND PAUL FOR PRESIDENT, INC.",
                "C00575795":"HILLARY FOR AMERICA",
                "C00577130":"BERNIE 2016",
                "C00577312":"CARLY FOR PRESIDENT",
                "C00577981":"HUCKABEE FOR PRESIDENT, INC.",
                "C00578245":"PATAKI FOR PRESIDENT INC",
                "C00578492":"SANTORUM FOR PRESIDENT 2016",
                "C00578658":"O'MALLEY FOR PRESIDENT",
                "C00578757":"LINDSEY GRAHAM 2016",
                "C00579458":"JEB 2016, INC.",
                "C00580100":"DONALD J. TRUMP FOR PRESIDENT, INC.",
                "C00580159":"JINDAL FOR PRESIDENT",
                "C00580399":"CHRIS CHRISTIE FOR PRESIDENT INC",
                "C00580480":"SCOTT WALKER INC",
                "C00581199":"JILL STEIN FOR PRESIDENT",
                "C00581215":"WEBB 2016",
                "C00581876":"KASICH FOR AMERICA INC",
                "C00582668":"GILMORE FOR AMERICA LLC",
                "C00583146":"LESSIG2016.US",
                "C00605568":"GARY JOHNSON 2016",
                "C00623884":"MCMULLIN FOR PRESIDENT COMMITTEE INC."}

df = pd.read_csv('virginia_contributions.csv')
df = df.drop("Unnamed: 18", axis=1)

df["cand_party"] = df["cand_id"].map(cand_party_dict)
df["cmte_nm"] = df["cmte_id"].map(cmte_nm_dict)

df.to_csv('virginia_contributions_mod.csv', index=False)