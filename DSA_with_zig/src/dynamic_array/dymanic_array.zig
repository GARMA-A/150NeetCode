const std = @import("std");

pub fn array(comptime T: type) type {
    return struct {
        data: []T,
        len: usize,
        alloc: std.mem.Allocator,

        const Self = @This();

        pub fn init(allocator: std.mem.Allocator, initial_capacity: usize) !Self {
            const data = try allocator.alloc(T, initial_capacity);
            return Self{
                .data = data,
                .len = 0,
                .alloc = allocator,
            };
        }

        pub fn deinit(self: *Self) void {
            self.alloc.free(T, self.data);
        }

        pub fn push(self: *Self, value: T) !void {
            if (self.len >= self.data.len) {
                const new_capacity = if (self.data.len == 0) 1 else self.data.len * 2;
                const new_data = try self.alloc.realloc(T, self.data, new_capacity);
                self.data = new_data;
            }
            self.data[self.len] = value;
            self.len += 1;
        }

        pub fn pop(self: *Self) ?T {
            if (self.len == 0) return null;
            self.len -= 1;
            return self.data[self.len];
        }
    };
}
