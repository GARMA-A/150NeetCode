const std = @import("std");

// pub fn array(comptime T: type) type {
//     return struct {
//         data: []T,
//         len: usize,
//         alloc: std.mem.Allocator,
//
//         const Self = @This();
//
//         pub fn init(allocator: std.mem.Allocator, initial_capacity: usize) !Self {
//             const data = try allocator.alloc(T, initial_capacity);
//             return Self{
//                 .data = data,
//                 .len = 0,
//                 .alloc = allocator,
//             };
//         }
//
//         pub fn deinit(self: *Self) void {
//             self.alloc.free(T, self.data);
//         }
//
//         pub fn push(self: *Self, value: T) !void {
//             if (self.len >= self.data.len) {
//                 const new_capacity = if (self.data.len == 0) 1 else self.data.len * 2;
//                 const new_data = try self.alloc.realloc(T, self.data, new_capacity);
//                 self.data = new_data;
//             }
//             self.data[self.len] = value;
//             self.len += 1;
//         }
//
//         pub fn pop(self: *Self) ?T {
//             if (self.len == 0) return null;
//             self.len -= 1;
//             return self.data[self.len];
//         }
//     };
// }

pub fn array(comptime T: type) type {
    return struct {
        data: *[]T,
        len: u64,
        capacity: u64,
        allocator: std.mem.Allocator,

        const Self = @This();

        pub fn init(allocator: std.mem.Allocator, capacity: ?u64) !Self {
            const data = try allocator.alloc(T, capacity orelse 10);
            return Self{ .data = data, .capacity = capacity orelse 10, .len = 0, .allocator = allocator };
        }

        pub fn deinit(self: *Self, allocator: std.mem.Allocator) Self {
            allocator.free(self.data);
        }
        pub fn push(self: *Self, value: T) !void {
            if (self.len == self.capacity) {
                self.data = try self.allocator.realloc(self.data, self.capacity * 2);
                self.capacity *= 2;
            }
            self.data[self.len] = value;
            self.len += 1;
        }

        pub fn pop(self: *Self) !T {
            if (self.len == 0) {
                return error{ArayIsEmpty};
            }
            self.len -= 1;
            return self.data[self.len + 1];
        }
    };
}

test "pop and push to dynamic array" {
    const gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer gpa.deinit();
    const allocator = gpa.allocator();
    const arr = try array(u8).init(allocator);
    defer arr.deinit(allocator);
    arr.push(12);
    arr.push(13);
    arr.push(14);
    std.testing.expect(arr.pop() == 14);
}
