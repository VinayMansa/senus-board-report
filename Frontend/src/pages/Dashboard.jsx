import {
    Grid,
    Typography,
    Paper,
} from "@mui/material";

import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import KPICard from "../components/KPICard";

import {
    getSummary,
} from "../services/dashboardService";

function Dashboard() {

    const [summary, setSummary] = useState(null);

    useEffect(() => {

        loadDashboard();

    }, []);

    const loadDashboard = async () => {

        const data = await getSummary();

        setSummary(data);

    };

    if (!summary)
        return <Typography>Loading...</Typography>;

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

                <Grid item xs={12} md={3}>
                    <KPICard
                        title="Reports"
                        value={summary.total_reports}
                    />
                </Grid>

                <Grid item xs={12} md={3}>
                    <KPICard
                        title="Processed"
                        value={summary.processed_reports}
                    />
                </Grid>

                <Grid item xs={12} md={3}>
                    <KPICard
                        title="Pending"
                        value={summary.pending_reports}
                    />
                </Grid>

                <Grid item xs={12} md={3}>
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
                >
                    Welcome to AI Powered Board Reporting
                </Typography>

                <Typography
                    mt={2}
                >
                    Backend successfully connected.
                </Typography>

            </Paper>

        </DashboardLayout>

    );

}

export default Dashboard;