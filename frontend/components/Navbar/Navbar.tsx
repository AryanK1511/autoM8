import React from 'react';
import Link from 'next/link';
import { Chip } from '@nextui-org/react';
import { Button } from '@nextui-org/react';
import { CheckIcon } from './CheckIcon';
import { UserIcon } from './UserIcon';
import Image from 'next/image';

// ========== NAVBAR COMPONENT ==========
export const Navbar: React.FC = () => {
  return (
    <nav className="bg-white">
      <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
        <div className="flex justify-between py-4">
          <div className="flex space-x-4">
            <div className="flex space-x-4">
              <Link href="/" className="flex items-center py-3 px-2">
                <Image
                  src="/images/navbar_logo.png"
                  width={150}
                  height={200}
                  alt="Picture of the author"
                />
              </Link>
            </div>
            <div className="flex items-center py-2 px-1">
              <Chip startContent={<CheckIcon size={18} />} variant="faded" color="success">
                v0.0.1
              </Chip>
            </div>
          </div>
          <div className="hidden md:flex items-center space-x-1">
            <Button
              className="text-customGreen border border-customGreen"
              variant="bordered"
              startContent={<UserIcon />}
            >
              Sign In
            </Button>
          </div>
          <div className="md:hidden flex items-center"></div>
        </div>
      </div>
    </nav>
  );
};
