import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
} from "recharts";

function KPIChart({ summary }) {

    const data = [
        {
            name: "Reports",
            value: summary.total_reports,
        },
        {
            name: "Processed",
            value: summary.processed_reports,
        },
        {
            name: "Pending",
            value: summary.pending_reports,
        },
        {
            name: "Metrics",
            value: summary.total_metrics,
        },
    ];

    return (

        <ResponsiveContainer
            width="100%"
            height={300}
        >

            <BarChart data={data}>

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar dataKey="value" />

            </BarChart>

        </ResponsiveContainer>

    );

}

export default KPIChart;