# simplex-pivot-analysis
This project compared the runtime of three different rules used in the Simplex method:

--**Bland's Rule**
--**Largest Subscript Rule**
--**Largest Coefficient Rule**

The goal was to find which pivoting rules gave the best performance, by finding the runtime across varying problem instance sizes using the three pivoting rules.
```
## Contents:
├── 📁 report
│   └── 📄 simplex_pivot_report.tex       # LaTeX source of the final report
│
├── 📁 data
│   └── 📄 timings.xlsx                   # Runtime data for each pivoting method
│
├── 📁 analysis
│   ├── 📄 pivot_analysis.xlsx            # Excel file processing raw timing data
│   ├── 📄 avg_runtime_plot.pdf           # Average runtime plot (by instance size)
│   └── 📄 worst_runtime_plot.pdf         # Worst runtime plot (by instance size)
│
├── 📁 code
│   ├── 📁 blands_rule                    # Python implementation of Bland's Rule
│   ├── 📁 largest_subscript_rule         # Python implementation of Largest Subscript Rule
│   └── 📁 largest_coefficient_rule       # Python implementation of Largest Coefficient Rule
│
└── 📄 README.md                          # Project description and documentation
```
