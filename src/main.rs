#![no_std]
#![no_main]

use core::panic::PanicInfo;
use core::ffi::c_void;

#[no_mangle]
pub extern "C" fn efi_main(_image_handle: *const c_void, _system_table: *const c_void) -> u64 {
    loop {}
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
