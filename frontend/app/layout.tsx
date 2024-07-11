import React from 'react';
import type { Metadata } from 'next';
import { UserProvider } from '@auth0/nextjs-auth0/client';
import { NextUIProvider } from '@nextui-org/react';
import { Navbar } from '@/components';
import './globals.css';

export const metadata: Metadata = {
  title: 'autoM8 | Effortless Automation',
  description: 'Effortless automation',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <UserProvider>
          <NextUIProvider>
            <Navbar />
            {children}
          </NextUIProvider>
        </UserProvider>
      </body>
    </html>
  );
}
