import {
    Paper,
    Typography,
    Button,
} from "@mui/material";

import { useState } from "react";

import { getSummaryAI } from "../services/aiService";

function AISummary() {

    const [summary, setSummary] =
        useState("");

    const generateSummary = async () => {

        const response =
            await getSummaryAI(4);

        setSummary(response.summary);

    };

    return (

        <Paper
            sx={{
                p: 3,
            }}
        >

            <Typography
                variant="h5"
            >
                AI Executive Summary
            </Typography>

            <Button
                variant="contained"
                sx={{
                    mt: 2,
                    mb: 2,
                }}
                onClick={generateSummary}
            >
                Generate Summary
            </Button>

            <Typography
                whiteSpace="pre-line"
            >
                {summary}
            </Typography>

        </Paper>

    );

}

export default AISummary;