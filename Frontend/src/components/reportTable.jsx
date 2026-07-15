import { DataGrid } from "@mui/x-data-grid";

const columns = [
    {
        field: "company",
        headerName: "Company",
        flex: 1,
    },
    {
        field: "title",
        headerName: "Report",
        flex: 2,
    },
    {
        field: "year",
        headerName: "Year",
        width: 120,
    },
    {
        field: "status",
        headerName: "Status",
        width: 150,
    },
    {
        field: "metrics",
        headerName: "Metrics",
        width: 120,
    },
];

function ReportTable({ reports }) {
    return (
        <div
            style={{
                height: 400,
                width: "100%",
            }}
        >
            <DataGrid
                rows={reports}
                columns={columns}
                pageSizeOptions={[5]}
            />
        </div>
    );
}

export default ReportTable;