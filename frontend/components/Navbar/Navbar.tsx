'use client';

import React from 'react';
import Link from 'next/link';
import { Chip } from '@nextui-org/react';
import { UserIcon, CheckIcon } from '@/components';
import Image from 'next/image';
import { useUser } from '@auth0/nextjs-auth0/client';
import { ProfileDropdown } from '@/components';

// ========== NAVBAR COMPONENT ==========
export const Navbar: React.FC = () => {
  // Getting the authenticated user if any
  const { user, error, isLoading }: any = useUser();

  return (
    <nav className="bg-transparent">
      <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
        <div className="flex justify-between py-4">
          <div className="flex space-x-4">
            <div className="flex space-x-4">
              <Link href="/" className="flex items-center py-3 px-2">
                <Image src="/images/navbar_logo.png" width={170} height={170} alt="autoM8 Logo" />
              </Link>
            </div>
            <div className="flex items-center py-2 px-1">
              <Chip
                className="px-2 py-4 shadow-lg shadow-green-500"
                startContent={<CheckIcon size={20} />}
                variant="shadow"
                color="success"
              >
                <span className="font-semibold text-lg">v0.0.1</span>
              </Chip>
            </div>
          </div>
          <div className="flex items-center space-x-1">
            {user ? (
              <ProfileDropdown />
            ) : (
              <Link href="/api/auth/login">
                <button className="inline-flex items-center px-4 py-2 shadow-lg shadow-indigo-400 bg-indigo-600 text-white  border border-indigo-600 shadow-sea rounded-md hover:bg-indigo-800">
                  <UserIcon />
                  <span className="text-lg font-semibold">Sign In</span>
                </button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};
