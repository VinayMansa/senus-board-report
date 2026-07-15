import {
    Box,
    Button,
    Paper,
    TextField,
    Typography,
} from "@mui/material";

import { useState } from "react";

import { loginUser } from "../services/authService";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";

function Login() {

    const navigate = useNavigate();

    const { login } = useAuth();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const handleLogin = async () => {

        try {
    
            const response = await loginUser(
                email,
                password
            );
    
            login(response.access_token);
    
            navigate("/dashboard");
    
        } catch (err) {
    
            console.log(err);
    
            alert("Invalid email or password");
        }
    
    };

    return (

        <Box
            sx={{
                height: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                bgcolor: "#f5f5f5",
            }}
        >

            <Paper
                sx={{
                    width: 400,
                    p: 4,
                }}
            >

                <Typography
                    variant="h4"
                    mb={3}
                    textAlign="center"
                >
                    Senus Board Reporting
                </Typography>

                <TextField
                    fullWidth
                    label="Email"
                    margin="normal"
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                />

                <TextField
                    fullWidth
                    type="password"
                    label="Password"
                    margin="normal"
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                />

                <Button
                    fullWidth
                    variant="contained"
                    sx={{ mt: 3 }}
                    onClick={handleLogin}
                >
                    Login
                </Button>

            </Paper>

        </Box>

    );
}

export default Login;