import {
    Grid,
    Typography,
    Paper,
} from "@mui/material";

import {
    useState,
    useEffect,
} from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import KPICard from "../components/KPICard";

import KPIChart from "../components/KPIChart";

import ReportTable from "../components/ReportTable";

import AISummary from "../components/AISummary";

import {
    getSummary,
    getReports,
} from "../services/dashboardService";

function Dashboard() {

    const [summary, setSummary] =
        useState();

    const [reports, setReports] =
        useState([]);

    useEffect(() => {

        loadDashboard();

    }, []);

    const loadDashboard =
        async () => {

            const summaryData =
                await getSummary();

            const reportData =
                await getReports();

            setSummary(summaryData);

            setReports(reportData);

        };

    if (!summary)
        return <Typography>
            Loading...
        </Typography>;

    return (

        <DashboardLayout>

            <Typography
                variant="h4"
                mb={4}
            >
                Dashboard
            </Typography>

            <Grid
                container
                spacing={3}
            >

                <Grid item xs={3}>
                    <KPICard
                        title="Reports"
                        value={summary.total_reports}
                    />
                </Grid>

                <Grid item xs={3}>
                    <KPICard
                        title="Processed"
                        value={summary.processed_reports}
                    />
                </Grid>

                <Grid item xs={3}>
                    <KPICard
                        title="Pending"
                        value={summary.pending_reports}
                    />
                </Grid>

                <Grid item xs={3}>
                    <KPICard
                        title="Metrics"
                        value={summary.total_metrics}
                    />
                </Grid>

            </Grid>

            <Paper
                sx={{
                    mt: 5,
                    p: 3,
                }}
            >

                <Typography
                    variant="h5"
                    mb={2}
                >
                    Financial Overview
                </Typography>

                <KPIChart
                    summary={summary}
                />

            </Paper>

            <Paper
                sx={{
                    mt: 5,
                    p: 3,
                }}
            >

                <Typography
                    variant="h5"
                    mb={2}
                >
                    Imported Reports
                </Typography>

                <ReportTable
                    reports={reports}
                />

            </Paper>

            <Paper
                sx={{
                    mt: 5,
                }}
            >

                <AISummary />

            </Paper>

        </DashboardLayout>

    );

}

export default Dashboard;