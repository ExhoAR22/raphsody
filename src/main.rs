#![no_std]
#![no_main]

use core::panic::PanicInfo;
use uefi::types::{Handle, SystemTable, Status};

#[no_mangle]
pub extern "C" fn efi_main(image_handle: Handle, system_table: *const SystemTable) -> Status {
    uefi::utils::init(image_handle, system_table);
    Status::Success
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
