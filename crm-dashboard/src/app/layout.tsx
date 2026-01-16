import type { Metadata } from "next";
import { Inter, Playfair_Display } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/Sidebar";

const inter = Inter({
    subsets: ["latin"],
    variable: "--font-inter",
});

const playfair = Playfair_Display({
    subsets: ["latin"],
    variable: "--font-playfair",
});

export const metadata: Metadata = {
    title: "Sales Pipeline 2026 | CRM Dashboard",
    description: "Sales CRM powered by Google Sheets",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body className={`${inter.variable} ${playfair.variable} antialiased transition-colors duration-300`}>
                <div className="flex min-h-screen">
                    <Sidebar />
                    <main className="flex-1 overflow-auto">
                        {children}
                    </main>
                </div>
            </body>
        </html>
    );
}
